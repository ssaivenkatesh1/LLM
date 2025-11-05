from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import BinaryIO
import io

from src.services.text_extractor import extract_text_from_pdf
from src.services.summarizer import Summarizer

app = FastAPI()

origins = [
    "*", # Allow all origins for development. Restrict in production.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check() -> dict:
    """Returns the health status of the API."""
    return {"status": "ok"}

summarizer_instance = Summarizer()

@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)) -> dict:
    """Summarizes an uploaded PDF file.

    Args:
        file (UploadFile): The PDF file to be summarized.

    Returns:
        dict: A dictionary containing the summary text and word counts.

    Raises:
        HTTPException: If the uploaded file is not a PDF, contains no text, or an internal error occurs.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are accepted.")

    try:
        file_content: BinaryIO = io.BytesIO(await file.read())
        extracted_text = extract_text_from_pdf(file_content)

        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="This document appears to contain no text. Please upload a text-based PDF.")

        summary_text = summarizer_instance.summarize(extracted_text)
        print(summary_text)

        return {
            "summary_text": summary_text,
            "original_word_count": len(extracted_text.split()),
            "summary_word_count": len(summary_text.split()),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process document: {e}")
