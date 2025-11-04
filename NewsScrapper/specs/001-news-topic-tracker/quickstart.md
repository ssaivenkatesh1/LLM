# Quickstart Guide

This guide provides instructions for setting up and running the Global News Topic Tracker locally.

## Running with Docker (Recommended)

This is the easiest way to get started.

1.  **Prerequisites**: Docker and `docker-compose` must be installed.
2.  **Environment Variables**: Create a `.env` file in the `backend` directory by copying the `.env.example` file and filling in your LLM API keys:
    ```bash
    cp backend/.env.example backend/.env
    ```
3.  **Build and Run**:
    From the root of the project, run:
    ```bash
    docker-compose up --build
    ```

-   The frontend will be available at `http://localhost:4200`.
-   The backend API will be available at `http://localhost:8000`.

## Manual Local Setup

---

## Prerequisites

-   Node.js 18+ and npm
-   Python 3.11+ and pip

## Backend Setup (Python/FastAPI)

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file by copying the `.env.example` file and adding your LLM API keys:
    ```bash
    cp .env.example .env
    ```

5.  **Initialize the database:**
    Run the following command from the `backend` directory to create the database and tables:
    ```bash
    python -c "from src.database import Base, engine; Base.metadata.create_all(bind=engine)"
    ```

6.  **Run the backend server:**
    ```bash
    uvicorn src.api.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## Frontend Setup (Angular)

1.  **Install Angular CLI (if not already installed):**
    ```bash
    npm install -g @angular/cli
    ```

2.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

3.  **Install dependencies:**
    ```bash
    npm install
    ```

4.  **Run the frontend development server:**
    ```bash
    ng serve
    ```
    The application will open in your browser at `http://localhost:4200`.

## Running the Scraper

The scraping process is triggered by clicking the "Refresh" button in the web UI, which calls the `POST /scrape` API endpoint.
