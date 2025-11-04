# vector_store.py
import os
import chromadb
from chromadb.config import Settings
import logging

logger = logging.getLogger(__name__)

# Default directory to persist Chroma DB
_CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")

def get_chroma_client(persist_dir: str = "./chroma_data"):
    # ✅ Use the new-style configuration
    client = chromadb.Client(Settings(
        persist_directory=persist_dir,
        is_persistent=True
    ))
    return client

def get_collection(client, name: str = "documents"):
    # ✅ get_or_create_collection is still valid
    return client.get_or_create_collection(name=name)
