# Quickstart

This document provides a quick guide to setting up and running the Meeting Note Taker application.

## Prerequisites

*   Python 3.11
*   Pip (Python package installer)
*   Ollama installed and running
*   A pulled Ollama model (e.g., `ollama pull gemma3`)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` will be created during the implementation phase)*

## Usage

### Processing an Audio File
To process a meeting audio file, use the `process-audio` command:
```bash
python -m src.cli process-audio /path/to/your/meeting.mp3
```

### Listing Notes
To see a list of all your generated notes:
```bash
python -m src.cli list-notes
```

### Viewing a Note
To view the content of a specific note:
```bash
python -m src.cli show-note <NOTE_ID>
```

### Editing a Note
To edit a note, which will open it in your default text editor:
```bash
python -m src.cli edit-note <NOTE_ID>
```
