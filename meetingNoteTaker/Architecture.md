# Architecture

## High-Level Requirements

The system must be able to:
*   Accept an audio file as input through a web interface or a command-line tool.
*   Transcribe the audio file to text.
*   Summarize the transcribed text to generate structured notes, including key decisions and action items.
*   Extract a list of tasks from the transcribed text.
*   Store the generated notes and tasks.
*   Allow users to view and edit the generated notes and tasks.
*   Perform all processing locally to ensure data privacy.

## High-Level Design

The system is designed with a frontend-backend architecture, and is also accessible via a command-line interface (CLI).

### Frontend

*   **Technology:** HTML, CSS, JavaScript
*   **Description:** A simple web interface that allows users to upload an audio file to the backend. It then displays the processed structured notes and tasks returned by the backend.

### Backend

*   **Technology:** Python, FastAPI, Uvicorn, Whisper, Ollama, SQLite
*   **Description:** A FastAPI server that exposes a REST API. The backend is responsible for:
    *   Handling file uploads from the frontend.
    *   Transcribing audio files using the Whisper model.
    *   Summarizing the transcribed text and extracting tasks using an Ollama-based model.
    *   Storing the processed data in a SQLite database.

### Command-Line Interface (CLI)

*   **Technology:** Python, argparse
*   **Description:** A command-line tool that provides the same functionality as the web interface, allowing users to process audio files directly from the terminal.

## Data Flow Diagram

```
+-----------------+      +-----------------+      +-----------------+
|   Frontend      |----->|   Backend API   |----->|   Processing    |
| (Upload Audio)  |      |  (FastAPI)      |      |   Services      |
+-----------------+      +-----------------+      +-----------------+
                                 |                      |
                                 |                      v
                                 |      +-----------------+
                                 |      |   Transcription |
                                 |      |    (Whisper)    |
                                 |      +-----------------+
                                 |                      |
                                 |                      v
                                 |      +-----------------+
                                 |      |  Summarization  |
                                 |      |    (Ollama)     |
                                 |      +-----------------+
                                 |                      |
                                 |                      v
                                 |      +-----------------+
                                 |      | Task Extraction |
                                 |      |    (Ollama)     |
                                 |      +-----------------+
                                 |                      |
                                 v                      |
                         +-----------------+      +-----------------+
                         |   Database      |<-----|   Processing    |
                         |   (SQLite)      |      |   Services      |
                         +-----------------+      +-----------------+
```

**Flow Description:**

1.  The user uploads an audio file via the **Frontend** or provides a file path via the **CLI**.
2.  The **Backend API** receives the audio file.
3.  The audio file is passed to the **Processing Services**.
4.  The **Transcription Service** uses Whisper to transcribe the audio to text.
5.  The transcribed text is passed to the **Summarization Service** and the **Task Extraction Service**, which use an Ollama-based model to generate structured notes and a task list.
6.  The processed data is stored in the **Database**.
7.  The structured notes and tasks are returned to the **Frontend** and displayed to the user.
