from fastapi import File, UploadFile, HTTPException,Depends, APIRouter,status,WebSocket,WebSocketDisconnect
from sqlalchemy.orm import Session
from config.database import get_db
from config import models,schemas
from config.oauth import get_current_user
import os
from chatbot.permission import verify_admin_user
from rag.models.chat_history import ChatHistory
from chatbot.rag_pipeline import get_qa_chain


router = APIRouter(
    prefix="/bot",
    tags=[
        'ChatBot'
    ]
)

chat_history = ChatHistory()
qa_chain=get_qa_chain()['qa_chain']
embeddings=get_qa_chain()['embeddings']
vectorstore=get_qa_chain()['vectorstore']

DOCUMENTS_FOLDER = "rag/documents"
os.makedirs(DOCUMENTS_FOLDER, exist_ok=True)

@router.post("/upload-pdf",response_model=schemas.DocumentRecordOut)
def upload_pdf(file: UploadFile = File(...),db:Session=Depends(get_db),current_user:models.User=Depends(verify_admin_user)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    try:

        file_path = os.path.join(DOCUMENTS_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.read())
        new_document=models.Document(
            filename=file.filename,
            file_path=file_path,
            user_id=current_user.id
        )
        db.add(new_document)
        db.commit()
        db.refresh(new_document)
        return new_document
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,detail=e.__str__())
    

@router.post('/ask',response_model=schemas.Answer)
def get_answer(question:schemas.Question,db:Session=Depends(get_db),current_user:models.User=Depends(get_current_user)):
    try:
        chat_id = f'user_{current_user.id}'
        # print("chat_id:",chat_id)
        previous_history = chat_history.retrieve_chat_history(chat_id)  

        if previous_history:
            conversation_context = "\n".join([item['message'] for item in previous_history])
            full_question = f"{conversation_context}\n{question.question}"
        else:
            full_question = question.question
        # relevant_documents = vectorstore.similarity_search(question.question, k=3)  
        # embeddings.index_documents(relevant_documents)
        # # Combine relevant documents with the question for the QA model
        # combined_input = f"{full_question}\n\nRelevant Documents:\n" + "\n".join([doc.page_content for doc in relevant_documents])
        answer_text=""
        answer = qa_chain.ask_question(full_question)
        if 'Helpful Answer:' in answer['result']:
            answer_text = answer['result'].split('Helpful Answer:')[1].strip()
        else:
            answer_text = answer['result']  #

        chat_history.upsert_message(chat_id, question.question, embeddings)
        chat_history.upsert_message(chat_id, answer_text, embeddings)

        return {
            "question":question.question,
            "answer":answer_text 
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail=str(e))




