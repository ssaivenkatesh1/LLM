# Application Architecture

This document outlines the high-level architecture and data flow of the Document Summarization Tool.

## High-Level Architecture

The application is designed as a containerized, multi-service system orchestrated by Docker Compose. It consists of two main services: a frontend web server and a backend API.

### Components

1.  **Frontend (Nginx Container)**:
    *   A lightweight Nginx server that serves the static HTML, CSS, and JavaScript files to the user's browser.
    *   Acts as a **reverse proxy** for the backend. All API calls from the frontend are routed through Nginx, which forwards them to the backend service. This is a standard pattern that simplifies cross-origin resource sharing (CORS) and decouples the frontend from the backend's location.

2.  **Backend (FastAPI Container)**:
    *   A Python application built with the FastAPI framework.
    *   Exposes a single API endpoint (`/summarize`) to handle file uploads and summarization requests.
    *   Contains the core business logic, including text extraction with `pdfplumber` and summarization using a local Hugging Face `transformers` model.

3.  **Hugging Face Cache (Docker Volume)**:
    *   To prevent re-downloading the large language model on every container start, a Docker volume is used.
    *   It maps the cache directory from the host machine (e.g., `~/.cache/huggingface`) to the appropriate location inside the backend container. This ensures the model is downloaded only once and is persisted.

### Architecture Diagram

```mermaid
graph TD
    subgraph User's Browser
        A[Client UI]
    end

    subgraph "Docker Environment (on Host Machine)"
        B[Nginx Container <br> Port 8080]
        C[Backend Container <br> (FastAPI)]
        D[(Hugging Face Cache <br> on Host)]

        A -- 1. Uploads PDF --> B
        B -- 2. Serves Static Files --> A
        B -- 3. Proxies API Request --> C
        C -- 4. Loads Model From --> D
        C -- 7. Sends Summary --> B
        B -- 8. Forwards Summary --> A
    end

    style D fill:#f9f,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
```

## Data Flow

Here is the step-by-step data flow for a typical summarization request:

1.  **User Interaction**: The user opens `http://localhost:8080` in their browser. Nginx serves the `index.html` and associated CSS/JS files.

2.  **File Upload**: The user selects a PDF file and clicks the "Summarize" button.

3.  **Frontend Request**: The browser's JavaScript sends a `POST` request containing the file data to `/api/summarize`. This request goes to the Nginx container.

4.  **Proxy Pass**: Nginx receives the request. Because the path starts with `/api/`, its configuration rules proxy the request internally to the `backend` service at `http://backend:8000/summarize`.

5.  **Backend Processing**: The FastAPI application receives the request.
    a.  The PDF file is read from the request body.
    b.  The `text_extractor` service uses `pdfplumber` to extract the text content from the PDF.
    c.  The `summarizer` service takes the extracted text and feeds it to the `facebook/bart-large-cnn` model, which is loaded from the mounted cache volume.
    d.  The model generates a summary.

6.  **Backend Response**: The FastAPI endpoint constructs a JSON response containing the summary text and word counts.

7.  **Proxy Response**: The backend sends the JSON response back to the Nginx container.

8.  **Frontend Update**: Nginx forwards the response to the user's browser. The JavaScript code receives the summary and dynamically updates the page to display it to the user.
