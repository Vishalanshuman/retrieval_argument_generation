from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

class DocumentCreator:

    def __init__(self, chunk_size=1000, chunk_overlap=200):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def create_documents_from_text(self, text):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        chunks = text_splitter.split_text(text)
        documents = [Document(page_content=chunk) for chunk in chunks]
        
        return documents
