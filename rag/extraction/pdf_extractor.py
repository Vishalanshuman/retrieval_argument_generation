import os
import fitz

class PDFExtractor:
    def __init__(self, pdf_folder="rag/documents"):
        """
        Initializes the PDFExtractor with the path to a folder containing PDFs.

        Args:
            pdf_folder (str): Path to the folder with PDF files.
        """
        self.pdf_folder = pdf_folder

    def extract_text_from_all_pdfs(self):
        """
        Extracts text from all PDF files in the specified folder.

        Returns:
            dict: A dictionary where keys are filenames and values are extracted text from each PDF.
        """
        if not os.path.exists(self.pdf_folder):
            raise FileNotFoundError(f"The folder at {self.pdf_folder} was not found.")
        
        pdf_texts = ""

        # Iterate over each file in the folder
        for filename in os.listdir(self.pdf_folder):
            file_path = os.path.join(self.pdf_folder, filename)
            
            # Process only PDF files
            if os.path.isfile(file_path) and filename.lower().endswith('.pdf'):
                try:
                    # Extract text from each PDF
                    pdf_texts+= f' {self.extract_text_from_pdf(file_path)}'
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
        
        return pdf_texts

    def extract_text_from_pdf(self, pdf_path):
        """
        Extracts text from a single PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: The extracted text from the PDF file.
        """
        try:
            doc = fitz.open(pdf_path)
        except fitz.FileDataError as e:
            raise Exception(f"Failed to open {pdf_path}. Ensure it's a valid PDF.") from e

        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        return text
