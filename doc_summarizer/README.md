# Document Summarization Tool

This project is a web-based tool that generates a concise summary from an uploaded PDF document.

## High-Level Requirement

A user wants to quickly understand the content of a PDF document without reading the whole text. They need a simple web interface to upload the document and receive a summary.

## Features

-   **PDF Upload**: A simple web interface to upload PDF files.
-   **Text Summarization**: Uses a local Hugging Face transformer model (`facebook/bart-large-cnn`) to generate a summary.
-   **Dockerized**: The entire application (frontend and backend) is containerized for easy setup and deployment.

## Technology Stack

-   **Backend**: Python, FastAPI
-   **Frontend**: HTML, CSS, JavaScript (Vanilla)
-   **Summarization**: `transformers` and `torch` libraries
-   **PDF Extraction**: `pdfplumber`
-   **Web Server/Proxy**: Nginx
-   **Containerization**: Docker, Docker Compose

## How to Run the Application

This project is fully containerized. The only prerequisite is to have Docker and Docker Compose installed.

1.  **Build and Run the Containers**:

    From the root directory of the project, run the following command:

    ```bash
    docker-compose up --build
    ```

    *Note: The first time you run this, it will download the multi-gigabyte summarization model, which may take a significant amount of time. This model will be cached on your host machine and reused on subsequent runs.*

2.  **Access the Application**:

    Once the containers are running, open your web browser and navigate to:

    **`http://localhost:8080`**

3.  **Use the Tool**:
    -   Click the "Choose File" button and select a PDF document.
    -   Click "Summarize PDF" to generate and view the summary.