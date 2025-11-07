# Meeting Note Taker

This project is a web application and command-line tool that converts meeting audio into structured notes and a task list. It uses the Whisper model for audio transcription and an Ollama-based model for summarization.

## Getting Started

### Prerequisites

*   Docker
*   Docker Compose

### Running the Application (Web UI)

1.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```

2.  **Access the web UI:**
    Open your web browser and navigate to `http://localhost:8080`.

### Stopping the Application

To stop the application and remove the containers, run the following command:
```bash
docker-compose down
```

## Command-Line Interface (CLI)

You can also use the command-line interface to process audio files.

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Run the CLI:**
    ```bash
    python -m src.cli.main process-audio /path/to/your/audio.mp3
    ```
    *(Note: You will need to have Python and the required dependencies installed on your local machine to run the CLI directly. You can install the dependencies by running `pip install -r requirements.txt` in the `backend` directory.)*
