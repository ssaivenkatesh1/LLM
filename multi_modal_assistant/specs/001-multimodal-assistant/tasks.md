# Tasks: Multimodal Assistant

**Input**: Design documents from `/specs/001-multimodal-assistant/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/`, `frontend/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create the `backend` and `frontend` directories.
- [X] T002 [P] Initialize the Python backend project in `backend/` with a `requirements.txt` file containing `fastapi`, `uvicorn`, `python-multipart`, and `llama-cpp-python`.
- [X] T003 [P] Initialize the Angular frontend project in `frontend/` using the Angular CLI and install Angular Material dependencies (`@angular/material`).
- [X] T004 [P] Create the basic directory structure for the backend in `backend/app/` as defined in `plan.md`.
- [X] T005 [P] Create the basic directory structure for the frontend in `frontend/src/` as defined in `plan.md`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T006 Create the `Dockerfile` for the backend in `backend/Dockerfile`.
- [X] T007 Create the `Dockerfile` for the frontend in `frontend/Dockerfile`.
- [X] T008 Create the `docker-compose.yml` file at the project root to orchestrate the `backend` and `frontend` services.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Get an answer from text and an image (Priority: P1) 🎯 MVP

**Goal**: Allow a user to submit a query with both an image and text and see the generated answer.

**Independent Test**: Can be tested by uploading an image, entering text, and verifying that an answer is displayed.

### Implementation for User Story 1

- [X] T009 [US1] Implement the basic FastAPI application setup in `backend/app/main.py`.
- [X] T010 [US1] Implement the model loading and prediction logic in `backend/app/services/model_service.py`.
- [X] T011 [US1] Implement the API endpoint for handling file uploads and text queries in `backend/app/api/endpoints/assistant.py`. This will use the `model_service`.
- [X] T012 [P] [US1] Create the main application component files in `frontend/src/app/app.component.ts` and `frontend/src/app/app.component.html`.
- [X] T013 [P] [US1] Create the `ImageUpload` component in `frontend/src/app/components/image-upload/` for uploading images.
- [X] T014 [P] [US1] Create the `QueryInput` component in `frontend/src/app/components/query-input/` for the text input and submit button.
- [X] T015 [US1] Implement the client-side logic in `frontend/src/app/app.component.ts` to call the backend API and display the result.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Get an answer from only text (Priority: P2)

**Goal**: Allow a user to submit a query with only text.

**Independent Test**: Can be tested by submitting a text-only query and verifying that an answer is displayed.

### Implementation for User Story 2

- [X] T016 [US2] Update the `assistant.py` endpoint in `backend/app/api/endpoints/assistant.py` to handle requests without an image.
- [X] T017 [US2] Update the `model_service.py` in `backend/app/services/model_service.py` to call the model with only text.
- [X] T018 [US2] Ensure the frontend in `frontend/src/app/app.component.ts` allows submitting the form with only text.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Get an answer from only an image (Priority: P3)

**Goal**: Allow a user to submit a query with only an image.

**Independent Test**: Can be tested by uploading an image without text and verifying that an answer is displayed.

### Implementation for User Story 3

- [X] T019 [US3] Update the `assistant.py` endpoint in `backend/app/api/endpoints/assistant.py` to handle requests without text.
- [X] T020 [US3] Update the `model_service.py` in `backend/app/services/model_service.py` to call the model with only an image.
- [X] T021 [US3] Ensure the frontend in `frontend/src/app/app.component.ts` allows submitting the form with only an image.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T022 [P] Implement user-friendly error handling on the frontend in `frontend/src/app/app.component.ts` for API errors or invalid file uploads.
- [X] T023 [P] Add loading indicators to the UI in `frontend/src/app/app.component.ts` while the model is processing the request.
- [X] T024 Add comprehensive logging to the backend services in `backend/app/`.
- [ ] T025 Validate the setup by following the instructions in `specs/001-multimodal-assistant/quickstart.md`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Stories (Phase 3-5)**: Depend on Foundational phase completion.
- **Polish (Phase 6)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2).
- **User Story 2 (P2)**: Can start after Foundational (Phase 2).
- **User Story 3 (P3)**: Can start after Foundational (Phase 2).

### Parallel Opportunities

- Tasks marked with `[P]` can be executed in parallel.
- Once the Foundational phase is complete, different developers can work on different user stories simultaneously.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Complete Setup + Foundational.
2. Add User Story 1 → Test independently.
3. Add User Story 2 → Test independently.
4. Add User Story 3 → Test independently.
