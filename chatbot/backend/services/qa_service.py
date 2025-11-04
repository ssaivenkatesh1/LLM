# qa_service.py
import os
import logging
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import Chroma as LangchainChroma
from langchain.embeddings import OpenAIEmbeddings

# Google-specific LangChain wrappers (optional)
try:
    from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
except Exception:
    GoogleGenerativeAI = None
    GoogleGenerativeAIEmbeddings = None

try:
    from langchain_community.llms import Ollama
except Exception:
    Ollama = None

try:
    from langchain_community.embeddings import OllamaEmbeddings
except Exception:
    OllamaEmbeddings = None

from backend.services.vector_store import get_chroma_client, get_collection

logger = logging.getLogger(__name__)

def get_vectorstore_and_embeddings():
    """
    Return a LangChain-compatible vectorstore (Chroma) and an embeddings object.
    """
    client = get_chroma_client()
    collection = get_collection(client)
    # LangChain's Chroma wrapper can use the chromadb client & collection name
    # Choose embeddings provider
    provider = os.getenv("EMBEDDING_PROVIDER", "").lower()
    if provider == "ollama" and OllamaEmbeddings:
        embeddings =  OllamaEmbeddings(
            model=os.getenv("OLLAMA_MODEL", "nomic-embed-text"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    elif provider == "google" and GoogleGenerativeAIEmbeddings and os.getenv("GOOGLE_API_KEY"):
        embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001"))
    elif os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
    else:
        # fallback to an attempt to use Google if available
        if GoogleGenerativeAIEmbeddings and os.getenv("GOOGLE_API_KEY"):
            embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001"))
        else:
            raise RuntimeError("No embedding provider configured. Set OPENAI_API_KEY or GOOGLE_API_KEY.")
    # Wrap chroma as LangChain vectorstore
    vectorstore = LangchainChroma(client=client, collection_name=collection.name, embedding_function=embeddings)
    return vectorstore, embeddings

def get_llm():
    """
    Return a configured LLM (LangChain wrapper) -- either OpenAI, Google (Gemini), or Ollama depending on env.
    """
    provider = os.getenv("LLM_PROVIDER", "").lower()
    if provider == "google" and GoogleGenerativeAI and os.getenv("GOOGLE_API_KEY"):
        return GoogleGenerativeAI(model=os.getenv("GOOGLE_LLM_MODEL", "gemini-pro"), temperature=float(os.getenv("TEMPERATURE", "0.1")))
    if provider == "ollama" and Ollama:
        return Ollama(
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            model=os.getenv("OLLAMA_LLM_MODEL", "llama2"), # Use OLLAMA_LLM_MODEL
        )
    if os.getenv("OPENAI_API_KEY"):
        # lazy import to avoid hard dependency errors if not installed
        from langchain import OpenAI
        return OpenAI(temperature=float(os.getenv("TEMPERATURE", "0.0")))
    # fallback error
    raise RuntimeError("No LLM provider configured. Set LLM_PROVIDER=google (with GOOGLE_API_KEY), LLM_PROVIDER=ollama, or configure OPENAI_API_KEY.")

def build_qa_chain():
    """
    Build a RetrievalQA chain with the configured vectorstore and LLM.
    """
    vectorstore, _ = get_vectorstore_and_embeddings()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = get_llm()

    # Use LangChain's RetrievalQA wrapper
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # for small context; consider "map_reduce" for very long docs
        retriever=retriever,
        return_source_documents=True
    )
    return qa

def answer_question(question: str, return_sources: bool = False):
    """
    Answer question using RAG. Returns the answer (and optionally source documents).
    """
    try:
        qa = build_qa_chain()
        result = qa({"query": question})
        answer = result.get("result") or result.get("answer") or ""
        if return_sources:
            sources = result.get("source_documents", [])
            # Convert source docs to simple dicts
            simple_sources = []
            for doc in sources:
                simple_sources.append({
                    "page_content": doc.page_content,
                    "metadata": doc.metadata
                })
            return {"answer": answer, "sources": simple_sources}
        return answer
    except Exception as e:
        logger.exception("Error answering question")
        return "Sorry — I couldn't answer that due to an internal error."
