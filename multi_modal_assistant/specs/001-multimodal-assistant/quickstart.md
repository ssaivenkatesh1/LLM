# Quickstart: Multimodal Assistant

**Date**: 2025-11-07
**Plan**: [plan.md](plan.md)

This guide provides the basic steps to get the Multimodal Assistant running locally using Docker.

## Prerequisites

-   Docker and Docker Compose installed.
-   A compatible multimodal model file (e.g., from the LLaVA family) available on your local machine.

## Running the Application

1.  **Configure the Model**:
    -   Place your downloaded multimodal model file in a directory of your choice.
    -   Update the `docker-compose.yml` file to mount this model file into the `backend` service. You will also need to set an environment variable to tell the backend where to find the model file.

    ```yaml
    # In docker-compose.yml
    services:
      backend:
        # ...
        environment:
          - MODEL_PATH=/models/your-model-file.gguf
        volumes:
          - /path/to/your/models:/models
    ```

2.  **Build and Run the Containers**:
    -   Open a terminal at the root of the project.
    -   Run the following command:

    ```bash
    docker-compose up --build
    ```

3.  **Access the Application**:
    -   Once the containers are running, open your web browser and navigate to `http://localhost:3000`.
    -   The frontend UI will be displayed, and you can interact with the assistant. The backend API will be available at `http://localhost:8000`.

## Project Structure

-   `backend/`: The Python FastAPI application that serves the API and runs the AI model.
-   `frontend/`: The React application that provides the web UI.
-   `docker-compose.yml`: Orchestrates the `frontend` and `backend` services.
