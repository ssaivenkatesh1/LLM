import os
import shutil
import logging
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# It's important to setup the logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Since the services are now under the backend directory, we can import them like this
from backend.services.document_processor import process_document
from backend.services.qa_service import answer_question

app = FastAPI(title="RAG Q&A Demo")

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploaded_docs")
os.makedirs(UPLOAD_DIR, exist_ok=True)

class AskRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Save file temporarily
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
        # guess file type from filename
        ext = file.filename.lower().split(".")[-1]
        n_chunks = process_document(file_location, ext, doc_id_prefix=file.filename)
        return {"status": "ok", "file": file.filename, "chunks_added": n_chunks}
    except Exception as e:
        logger.exception("Upload failed")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/ask")
async def ask_question_endpoint(request: AskRequest):
    resp = answer_question(request.question, return_sources=True)
    return resp

@app.get("/")
def read_root():
    return {"Hello": "World"}