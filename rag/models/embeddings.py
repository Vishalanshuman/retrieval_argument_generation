from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class EmbeddingModel:


    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):

        self.model_name = model_name
        self.vectorstore = None

    def index_documents(self, documents):
 
        embeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        
        # Create vector store from the documents
        self.vectorstore = FAISS.from_documents(documents, embeddings)
        
    def get_vectorstore(self):

        if not self.vectorstore:
            raise Exception("Vector store is not initialized. Index documents first.")
        
        return self.vectorstore
