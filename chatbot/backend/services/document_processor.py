# document_processor.py
import logging
import os
from typing import List, Dict, Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter

# Try to import embeddings. We'll support OpenAI and Google generative embeddings.
try:
    from langchain.embeddings import OpenAIEmbeddings
except Exception:
    OpenAIEmbeddings = None

try:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
except Exception:
    GoogleGenerativeAIEmbeddings = None

# ✅ NEW: import Ollama embeddings from LangChain community module
try:
    from langchain_community.embeddings import OllamaEmbeddings
except Exception:
    OllamaEmbeddings = None

from .vector_store import get_chroma_client, get_collection

logger = logging.getLogger(__name__)

# Text extraction helpers
def extract_text_from_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def extract_text_from_md(path: str) -> str:
    return extract_text_from_txt(path)

def extract_text_from_pdf(path: str) -> str:
    try:
        import pdfplumber
    except ImportError:
        raise RuntimeError("pdfplumber is required to extract text from PDFs (pip install pdfplumber)")
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                text_parts.append(t)
    return "\n\n".join(text_parts)

def extract_text_from_docx(path: str) -> str:
    try:
        import docx
    except ImportError:
        raise RuntimeError("python-docx is required to extract text from DOCX (pip install python-docx)")
    doc = docx.Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text]
    return "\n\n".join(paragraphs)

def extract_text(file_path: str, file_type: str) -> str:
    file_type = file_type.lower()
    if file_type in ("txt", "text/plain"):
        return extract_text_from_txt(file_path)
    if file_type in ("md", "markdown"):
        return extract_text_from_md(file_path)
    if file_type == "pdf":
        return extract_text_from_pdf(file_path)
    if file_type in ("docx",):
        return extract_text_from_docx(file_path)
    raise ValueError(f"Unsupported file type: {file_type}")

def choose_embeddings():
    """
    Choose embeddings implementation based on available packages and env vars.
    Preference order: GoogleGenerativeAIEmbeddings (if env configured) -> OpenAIEmbeddings
    """
    # If user explicitly sets provider via env var, honor it
    provider = os.getenv("EMBEDDING_PROVIDER", "").lower()
    if provider == "ollama" and OllamaEmbeddings:
        return OllamaEmbeddings(
            model=os.getenv("OLLAMA_MODEL", "nomic-embed-text"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    elif provider == "google" and GoogleGenerativeAIEmbeddings:
        return GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001"))
    elif provider == "openai" and OpenAIEmbeddings:
        return OpenAIEmbeddings()
    # Default preferences
    elif GoogleGenerativeAIEmbeddings and os.getenv("GOOGLE_API_KEY"):
        return GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001"))
    elif OpenAIEmbeddings and os.getenv("OPENAI_API_KEY"):
        return OpenAIEmbeddings()
    raise RuntimeError("No embedding provider available. Set EMBEDDING_PROVIDER env or install/ configure OpenAI/Google SDKs.")

def process_document(file_path: str, file_type: str, doc_id_prefix: Optional[str] = None, metadata: Optional[Dict] = None):
    """
    Process an uploaded document:
      - extract text
      - split into chunks
      - embed chunks
      - store in Chroma
    """
    logger.info(f"Processing document {file_path} (type={file_type})")
    if metadata is None:
        metadata = {}

    text = extract_text(file_path, file_type)
    if not text.strip():
        logger.warning("No text extracted from document")
        return 0

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    logger.info(f"Split into {len(chunks)} chunks")

    embeddings_client = choose_embeddings()

    # Generate embeddings (LangChain embedding object usually has embed_documents)
    try:
        embedded = embeddings_client.embed_documents(chunks)
    except Exception as e:
        logger.exception("Failed to generate embeddings")
        raise

    # Store in Chroma
    client = get_chroma_client()
    coll = get_collection(client)
    ids = []
    metadatas = []
    for i, chunk in enumerate(chunks):
        id = f"{doc_id_prefix or os.path.basename(file_path)}_{i}"
        ids.append(id)
        mm = metadata.copy()
        mm.update({"source": file_path, "chunk_index": i})
        metadatas.append(mm)

    coll.add(embeddings=embedded, documents=chunks, ids=ids, metadatas=metadatas)
    # persist (Chroma will manage persistence automatically if configured)
    logger.info(f"Stored {len(chunks)} chunks to Chroma collection '{coll.name}'")
    return len(chunks)
