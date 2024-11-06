import os
from fastapi import HTTPException,status
from dotenv import load_dotenv
from rag.models.document_creator import DocumentCreator
from  rag.models.embeddings import EmbeddingModel
from rag.extraction.pdf_extractor import PDFExtractor
from rag.qa.retrieval_qa import RetrievalQAChain
from rag.models.chat_history import ChatHistory
from rag.utils.logger import Logger
from rag.config.settings import Settings

load_dotenv()

logger = Logger(log_name="rag_application.log").get_logger()

def get_qa_chain():
    try:
        logger.info("Starting RAG application pipeline.")
        setting = Settings()

        chat_history = ChatHistory()
        chat_id = "unique_chat_id"  # Unique chat session identifier
        embedding_model = setting.embedding_model
        qa_model = setting.model_name

        document_extractor = PDFExtractor()
        text = document_extractor.extract_text_from_all_pdfs()

        document_creator = DocumentCreator()
        documents = document_creator.create_documents_from_text(text)
        logger.info("Documents created successfully from PDF.")

        embeddings = EmbeddingModel(model_name=embedding_model)
        index_document = embeddings.index_documents(documents)
        vectorstore = embeddings.get_vectorstore()
        logger.info("Document embeddings generated and indexed successfully.")

        qa_chain = RetrievalQAChain(model_name=qa_model, vectorstore=vectorstore)
        qa_chain.setup_qa_chain()
        logger.info("Retrieval QA chain setup successfully.")
        return {"qa_chain":qa_chain,"embeddings":embeddings,'vectorstore':vectorstore}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,detail=e.__str__())
