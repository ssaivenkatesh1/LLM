# Tasks: Document Summarization Tool

**Input**: Design documents from `/specs/001-doc-summarization-tool/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Phase 1: Project Setup

**Purpose**: Create the initial directory structure and configuration for the backend and frontend.

- [X] T001 Create the project directory structure (`backend/src/api`, `backend/src/services`, `backend/tests`, `frontend/css`, `frontend/js`) as defined in `plan.md`.
- [X] T002 [P] Create the backend dependency file at `backend/requirements.txt` and add `fastapi`, `uvicorn[standard]`, `python-multipart`, `pdfplumber`, `torch`, and `transformers`.
- [X] T003 [P] Create the main frontend file at `frontend/index.html`.
- [X] T004 [P] Create an empty stylesheet at `frontend/css/style.css`.
- [X] T005 [P] Create an empty JavaScript file at `frontend/js/app.js`.
- [X] T006 [P] Create an empty API entrypoint file at `backend/src/api/main.py`.
- [X] T007 [P] Create an empty service file at `backend/src/services/text_extractor.py`.
- [X] T008 [P] Create an empty service file at `backend/src/services/summarizer.py`.

---

## Phase 2: Foundational (Backend API)

**Purpose**: Set up a basic, runnable web server that the frontend can communicate with.

- [X] T009 In `backend/src/api/main.py`, implement a basic FastAPI application.
- [X] T010 In `backend/src/api/main.py`, add CORS middleware to allow requests from the frontend.
- [X] T011 In `backend/src/api/main.py`, create a health check endpoint at `/health` that returns a 200 OK response.

**Checkpoint**: The backend server can be started, and the frontend can successfully make requests to the `/health` endpoint.

---

## Phase 3: User Story 1 - Successful Summarization (Priority: P1) 🎯 MVP

**Goal**: A user can upload a valid PDF and see a generated summary.

**Independent Test**: Open `frontend/index.html`, upload a text-based PDF, and verify that a summary text appears on the screen.

### Implementation for User Story 1

- [X] T012 [P] [US1] In `backend/src/services/text_extractor.py`, implement a function that takes a file-like object and returns the extracted text using `pdfplumber`.
- [X] T013 [P] [US1] In `backend/src/services/summarizer.py`, implement the summarization logic. This includes loading the `facebook/bart-large-cnn` model, tokenizing, chunking text to fit model limits, and generating the summary.
- [X] T014 [US1] In `backend/src/api/main.py`, implement the `POST /summarize` endpoint. It should use the text extractor and summarizer services and return the summary as JSON. (Depends on T012, T013)
- [X] T015 [P] [US1] In `frontend/index.html`, create the UI with a file input (`<input type="file">`), a button, and a `<div>` to display results.
- [X] T016 [US1] In `frontend/js/app.js`, add an event listener to the button. On click, it should send the selected file to the `/summarize` endpoint and display the returned summary in the results `<div>`. (Depends on T015)
- [X] T017 [P] [US1] In `frontend/css/style.css`, add basic styling to make the UI clean and usable.

**Checkpoint**: The MVP is complete. The core feature of uploading a PDF and viewing a summary is functional.

---

## Phase 4: User Story 2 - Invalid File Type (Priority: P2)

**Goal**: The system gracefully handles uploads of non-PDF files.

**Independent Test**: Attempt to upload a `.jpg` or `.txt` file and verify that a user-friendly error message is displayed.

### Implementation for User Story 2

- [X] T018 [US2] In `backend/src/api/main.py`, add validation to the `/summarize` endpoint to check the `content_type` of the uploaded file. If it is not `application/pdf`, return a 400 HTTP error with a clear error message.
- [X] T019 [P] [US2] In `frontend/index.html`, add the `accept=".pdf"` attribute to the file input to guide users to select the correct file type.
- [X] T020 [US2] In `frontend/js/app.js`, enhance the `fetch` logic to handle non-200 responses and display the error message from the backend to the user. (Depends on T018)

**Checkpoint**: The application is now more robust by providing clear feedback for invalid user input.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements to code quality, documentation, and error handling.

- [X] T021 [P] Add docstrings and type hints to all public functions in the `backend/` directory.
- [X] T022 [P] Create a `README.md` in the root directory, consolidating setup and usage instructions from `quickstart.md`.
- [X] T023 In `backend/src/api/main.py`, add exception handling around the service calls in the `/summarize` endpoint to catch and log any errors during text extraction or summarization.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1.
- **Phase 3 (US1)** and **Phase 4 (US2)** both depend on Phase 2. They can be worked on in parallel after Phase 2 is complete, but US1 is the priority.
- **Phase 5 (Polish)** can be done after all user stories are complete.

### Parallel Opportunities

- **Within Setup**: Tasks T002-T008 can be done in parallel.
- **User Stories**: After Phase 2 is done, different developers could work on Phase 3 and Phase 4 simultaneously.
- **Within US1**: Backend (T012, T013) and Frontend (T015, T017) tasks can be developed in parallel. T014 and T016 create the integration points.
