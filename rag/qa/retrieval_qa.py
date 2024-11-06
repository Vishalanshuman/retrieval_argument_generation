import os
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub

class RetrievalQAChain:

    def __init__(self, model_name="mistralai/Mixtral-8x7B-Instruct-v0.1", vectorstore=None):

        self.model_name = model_name
        self.vectorstore = vectorstore
        self.qa_chain = None
        self.huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    
    def setup_qa_chain(self):

        if not self.vectorstore:
            raise Exception("Vector store is not initialized. Please provide a valid vector store.")
        
        # Set up the retriever from the vector store
        retriever = self.vectorstore.as_retriever()

        # Initialize the language model with HuggingFaceHub
        llm = HuggingFaceHub(repo_id=self.model_name, huggingfacehub_api_token=self.huggingface_token)
        
        # Create the QA chain with the language model and retriever
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm, retriever=retriever
        )
    
    def ask_question(self, question):

        if not self.qa_chain:
            raise Exception("QA chain is not initialized. Run setup_qa_chain() first.")
        
        answer = self.qa_chain.invoke(question)
        return answer
