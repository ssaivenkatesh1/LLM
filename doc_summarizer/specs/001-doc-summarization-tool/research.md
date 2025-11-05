# Research & Decisions

This document outlines key technical decisions made to resolve ambiguities during the planning phase.

## 1. Data Storage

- **Decision**: No data persistence will be implemented for the initial version.
- **Rationale**: The core requirement is to upload a PDF and receive a summary. Storing documents or summaries adds unnecessary complexity and cost for the MVP. All processing will be done in-memory per request.
- **Alternatives Considered**:
  - **File System Storage**: Rejected as it would require managing storage and cleanup processes.
  - **Database (SQLite/PostgreSQL)**: Rejected as it introduces significant overhead for a feature that does not require data retention.

## 2. Frontend Framework

- **Decision**: The frontend will be built using vanilla JavaScript, HTML, and CSS.
- **Rationale**: The user interface is simple: a file upload form and a display area for the summary text. A full-fledged framework like React or Vue would be overkill and introduce a larger build process and dependency footprint. Vanilla JS is sufficient, lightweight, and fast for this purpose.
- **Alternatives Considered**:
  - **React/Vue**: Rejected due to unnecessary complexity for the project's scope.
  - **Server-Side Rendering (e.g., with Jinja2)**: Rejected to keep the backend a stateless API, which is more scalable and simplifies development.

## 3. PDF Text Extraction

- **Decision**: Use the `pdfplumber` library as specified.
- **Rationale**: `pdfplumber` is a well-regarded library for extracting text and metadata from PDFs, and it works well for machine learning applications.

## 4. Summarization Model

- **Decision**: Use the `facebook/bart-large-cnn` model locally via `transformers` and `torch`.
- **Rationale**: The user explicitly requested a local model to avoid API dependencies. This model provides a good balance of performance and summary quality. The plan includes a chunking strategy to handle the model's input token limit.
