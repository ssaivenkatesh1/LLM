# Chatbot Application

## Overview

This is a question-answering chatbot application built using a Retrieval-Augmented Generation (RAG) architecture. The application allows users to ask questions and receive answers based on a set of documents.

The tech stack includes:
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: ChromaDB for vector storage and retrieval

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Getting Started

To start the application, run the following command from the root directory of the project:

```bash
docker-compose up -d
```

This will build the Docker images and start the frontend, backend, and database services in detached mode.

Once the services are running, you can access the chatbot interface by navigating to `http://localhost:8501` in your web browser.

## Stopping the Application

To stop the application and remove the containers, run the following command:

```bash
docker-compose down
```

## Services

The application consists of three main services orchestrated by `docker-compose`:

| Service    | Port      | Description                                       |
|------------|-----------|---------------------------------------------------|
| `frontend` | `8501`    | The Streamlit user interface for the chatbot.     |
| `backend`  | `8001`    | The FastAPI server providing backend logic.       |
| `chromadb` | `8000`    | The ChromaDB instance for vector storage.         |
