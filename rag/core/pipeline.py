import os
from rag.extraction.pdf_extractor import PDFExtractor
from rag.models.document_creator import DocumentCreator
from rag.models.embeddings import EmbeddingModel
from rag.qa.retrieval_qa import RetrievalQA
from rag.config.settings import Settings
from rag.utils.logger import get_logger

logger = get_logger(__name__)

class RAGPipeline:

    def __init__(self):
        self.settings = Settings()
        self.pdf_extractor = PDFExtractor(self.settings.pdf_path)
        self.document_creator = DocumentCreator(self.settings.chunk_size, self.settings.chunk_overlap)
        self.embedding_model = EmbeddingModel(self.settings.embedding_model)
        self.retrieval_qa = None

    def run_pipeline(self, question):
        text = self.pdf_extractor.extract_text()
        logger.info("Text extracted successfully.")
        
        documents = self.document_creator.create_documents_from_text(text)
        self.embedding_model.index_documents(documents)
        
        self.retrieval_qa = RetrievalQA(self.embedding_model.vectorstore, self.settings.model_name)
        answer = self.retrieval_qa.ask_question(question)
        
        return answer
