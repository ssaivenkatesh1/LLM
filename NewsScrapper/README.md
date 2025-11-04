# NewsScrapper

This project consists of a backend (Python FastAPI) and a frontend (React) application designed to scrape news, identify trending topics, and summarize articles using Large Language Models (LLMs).

## Project Structure

```
.
├── backend/
├── frontend/
├── docker-compose.yml
├── GEMINI.md
├── README.md
└── ...
```

## Technologies Used

*   **Backend:** Python 3.11+, FastAPI, SQLAlchemy, BeautifulSoup4, Requests, Google Generative AI (Gemini), OpenAI.
*   **Frontend:** Node.js 18+, React, Axios.
*   **Database:** SQLite (managed via SQLAlchemy).
*   **Containerization:** Docker, Docker Compose.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Docker and Docker Compose installed on your system.
*   Python 3.11+ (for local development/script execution, though Docker handles most of this).
*   Node.js 18+ (for local frontend development, though Docker handles most of this).
*   API Keys for Google Gemini and OpenAI. These should be set as environment variables.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd NewsScrapper
    ```

2.  **Set up Environment Variables:**
    Create a `.env` file in the `backend/` directory with your API keys:
    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```
    Replace `YOUR_GEMINI_API_KEY` and `YOUR_OPENAI_API_KEY` with your actual API keys.

### Running the Application

The application uses Docker Compose to manage both the backend and frontend services.

1.  **Start the services:**
    Navigate to the root directory of the project (where `docker-compose.yml` is located) and run:
    ```bash
    docker-compose up --build
    ```
    This command will:
    *   Build the Docker images for both backend and frontend (if not already built or if changes are detected).
    *   Start the `db-migrator` service to create database tables.
    *   Start the `backend` service (accessible at `http://localhost:8000`).
    *   Start the `frontend` service (accessible at `http://localhost:4200`).

2.  **Access the Frontend:**
    Open your web browser and go to `http://localhost:4200`.

3.  **Trigger Scraping and Summarization:**
    On the frontend, click the "Refresh" button. This will:
    *   Clear all existing data in the database.
    *   Scrape the latest news articles.
    *   Identify the first 10 article titles as topics.
    *   Summarize the content of each article using the configured LLM (Gemini by default).
    *   Display the article titles (as clickable links) and their summaries.

### Stopping the Application

To stop all running services and remove their containers, networks, and volumes:

```bash
docker-compose down
```

### Database Management

#### Clearing all data and resetting tables

To completely clear all data from the database and recreate the tables, you can run the `reset_db.py` script inside the backend Docker container. This is automatically done when you click the "Refresh" button in the frontend, but you can also do it manually:

1.  **Ensure Docker containers are running:**
    ```bash
    docker-compose up -d
    ```
2.  **Find the backend container name:**
    ```bash
    docker ps
    ```
    Look for the container with the image `newsscrapper-backend` (e.g., `newsscrapper-backend-1`).

3.  **Execute the reset script inside the container:**
    Replace `newsscrapper-backend-1` with your actual backend container name.
    ```bash
    docker exec newsscrapper-backend-1 python -m src.reset_db
    ```

## Development

### Backend

*   **Location:** `backend/`
*   **Run locally (without Docker):**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn src.api.main:app --reload --port 8000
    ```
*   **Tests:**
    ```bash
    cd backend
    pytest
    ```

### Frontend

*   **Location:** `frontend/`
*   **Run locally (without Docker):**
    ```bash
    cd frontend
    npm install
    npm start
    ```
