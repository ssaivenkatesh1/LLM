# Task List: Meeting Audio to Structured Notes and Task List

**Branch**: `001-audio-to-notes` | **Date**: November 6, 2025 | **Spec**: [spec.md](spec.md)

## Phase 1: Backend Setup

- [ ] T001 Create the backend project structure: `backend/src/models`, `backend/src/services`, `backend/src/api`, `backend/tests`.
- [ ] T002 Create a `requirements.txt` file in the `backend` directory.
- [ ] T003 Add `fastapi`, `uvicorn`, `python-multipart`, `whisper`, `ollama`, and `pytest` to `backend/requirements.txt`.
- [ ] T004 [P] Create a database setup script in `backend/src/lib/database.py` to initialize the SQLite database and create the necessary tables.
- [ ] T005 [P] Move the data models from `src/models` to `backend/src/models`.
- [ ] T006 [P] Move the services (`transcription.py`, `summarization.py`, `task_extraction.py`) to `backend/src/services`.

## Phase 2: Backend API Implementation

- [ ] T007 [US1] Create the FastAPI application in `backend/src/api/main.py`.
- [ ] T008 [US1] Implement the `/upload-audio/` endpoint in `backend/src/api/main.py`.
- [ ] T009 [US1] Integrate the transcription, summarization, and task extraction services into the `/upload-audio/` endpoint.
- [ ] T010 [US1] Implement the logic to save the processed data to the database.

## Phase 3: Frontend Setup

- [ ] T011 Create the frontend project structure: `frontend/src`, `frontend/tests`.
- [ ] T012 Create an `index.html` file in `frontend/src`.
- [ ] T013 Create a `style.css` file in `frontend/src`.
- [ ] T014 Create a `script.js` file in `frontend/src`.

## Phase 4: Frontend Implementation

- [ ] T015 [US1] Create the HTML structure in `index.html` for the file upload form.
- [ ] T016 [US1] Style the file upload form in `style.css`.
- [ ] T017 [US1] Implement the JavaScript logic in `script.js` to handle file uploads to the backend API.
- [ ] T018 [US1] Display the processed notes and tasks returned from the backend.

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T019 Implement robust error handling for the backend API.
- [ ] T020 [P] Add verbose logging to the backend API.
- [ ] T021 [P] Implement a progress indicator on the frontend to show the status of the audio processing.

## Dependencies

- Backend API Implementation depends on Backend Setup.
- Frontend Implementation depends on Frontend Setup and Backend API Implementation.

## Parallel Execution

- Backend and Frontend setup can be done in parallel.
- Within the backend, database setup and moving models/services can be done in parallel.
- Within the frontend, HTML, CSS, and JS can be developed in parallel to some extent.

## Implementation Strategy

The implementation will follow a backend-first approach. The backend API will be implemented and tested first, followed by the frontend.