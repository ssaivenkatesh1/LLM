import pdfplumber
from typing import BinaryIO

def extract_text_from_pdf(file_object: BinaryIO) -> str:
    """Extracts text from a PDF file-like object using pdfplumber.

    Args:
        file_object (BinaryIO): A file-like object containing the PDF content.

    Returns:
        str: The extracted text content from the PDF.
    """
    text_content = []
    with pdfplumber.open(file_object) as pdf:
        for page in pdf.pages:
            text_content.append(page.extract_text())
    return "\n".join(filter(None, text_content))
