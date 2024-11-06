import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    pdf_path = os.getenv("PDF_PATH", "resume.pdf")
    model_name = os.getenv("MODEL_NAME", "mistralai/Mixtral-8x7B-Instruct-v0.1")
    embedding_model = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    chunk_size = int(os.getenv("CHUNK_SIZE", 1000))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 200))
    huggingface_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
