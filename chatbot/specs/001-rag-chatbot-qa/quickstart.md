# Quickstart

This document provides instructions on how to set up and run the chatbot application.

## Prerequisites

-   Python 3.11
-   Docker (for ChromaDB)

## Application Setup

1.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn python-multipart langchain chromadb streamlit
    ```
2.  **Run ChromaDB**:
    ```bash
    docker run -p 8000:8000 chromadb/chroma
    ```
3.  **Run the application**:
    ```bash
    streamlit run src/app.py
    ```

## Running the Application

1.  Start the ChromaDB container.
2.  Run the Streamlit application.
3.  Open your browser and navigate to the URL provided by Streamlit.