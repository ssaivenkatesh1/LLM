# Multi-Modal Assistant

This project is a multi-modal assistant that can process both text and images. It consists of a Python backend powered by FastAPI and an Angular frontend.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python:** 3.11+
- **Node.js:** 20.x+
- **npm:** 10.x+

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd multi-modal-assistant
    ```

2.  **Backend Setup:**
    - Navigate to the backend directory:
      ```bash
      cd backend
      ```
    - Create and activate a virtual environment (recommended):
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
      ```
    - Install the required Python packages:
      ```bash
      pip install -r requirements.txt
      ```

3.  **Frontend Setup:**
    - Navigate to the frontend directory:
      ```bash
      cd ../frontend
      ```
    - Install the required Node.js packages:
      ```bash
      npm install
      ```

## Running the Application

1.  **Start the Backend Server:**
    - In the `backend` directory, run the following command:
      ```bash
      uvicorn app.main:app --reload
      ```
    - The backend API will be running at `http://127.0.0.1:8000`.

2.  **Start the Frontend Application:**
    - In the `frontend` directory, run the following command:
      ```bash
      npm start
      ```
    - The frontend application will be running at `http://localhost:4200`.

## Accessing the Application

Once both the backend and frontend are running, you can access the application by opening your web browser and navigating to:

[http://localhost:4200](http://localhost:4200)

## Stopping the Application

To stop the application, press `Ctrl+C` in each of the terminal windows where the backend and frontend servers are running.
