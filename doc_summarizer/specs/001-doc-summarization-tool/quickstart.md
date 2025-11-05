# Quickstart Guide

This guide provides instructions on how to set up and run the Document Summarization Tool locally.

## Prerequisites

- Python 3.10+
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install backend dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Download the summarization model**:
    The first time you run the application, the `transformers` library will automatically download the `facebook/bart-large-cnn` model. This may take some time and requires an internet connection.

## Running the Application

1.  **Start the backend server**:
    ```bash
    uvicorn backend.src.api.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

2.  **Launch the frontend**:
    Open the `frontend/index.html` file in your web browser.

3.  **Use the tool**:
    - Click the "Choose File" button and select a PDF document.
    - Click "Summarize" to generate and view the summary.

## Running with Docker (Optional)

If you have Docker installed, you can build and run the application in a container.

1.  **Build the Docker image**:
    ```bash
    docker build -t doc-summarizer .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8000:8000 doc-summarizer
    ```
    The application will be accessible at `http://127.0.0.1:8000`.
