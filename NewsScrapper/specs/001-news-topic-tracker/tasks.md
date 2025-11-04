# Tasks: Global News Topic Tracker

**Input**: Design documents from `/specs/001-news-topic-tracker/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create root `docker-compose.yml` file.
- [x] T002 Create `backend/` directory with `Dockerfile` and `requirements.txt`.
- [x] T003 Create `frontend/` directory with `Dockerfile` and `package.json`.
- [x] T004 Create `.env.example` in `backend/` for environment variables.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T005 [P] Initialize FastAPI app in `backend/src/api/main.py`.
- [x] T006 [P] Set up database connection and session management in `backend/src/database.py`.
- [x] T007 [P] Create base data models (SQLAlchemy) in `backend/src/models/` based on `data-model.md`.
- [x] T008 [P] Initialize basic Angular app structure in `frontend/src/app/`.
- [x] T009 [P] Set up API client service in `frontend/src/app/services/api.service.ts`.

---

## Phase 3: User Story 1 - View Trending Topics (Priority: P1) 🎯 MVP

**Goal**: Display a list of trending topics with their summaries.

**Independent Test**: The frontend should display a list of topics and summaries fetched from the backend.

### Implementation for User Story 1

- [x] T010 [US1] Implement `GET /topics` endpoint in `backend/src/api/routes/topics.py`.
- [x] T011 [US1] Implement service logic to fetch topics and summaries from the database in `backend/src/services/topic_service.py`.
- [x] T012 [P] [US1] Create `TopicListComponent` in `frontend/src/app/components/topic-list/topic-list.component.ts`.
- [x] T013 [P] [US1] Create main `HomeComponent` in `frontend/src/app/components/home/home.component.ts` to display the `TopicListComponent`.
- [x] T014 [US1] Fetch and display topics in the `HomeComponent`.

---

## Phase 4: User Story 3 - Manually Refresh Topics (Priority: P1)

**Goal**: Allow the user to manually trigger a new scrape and summarization process.

**Independent Test**: Clicking the "Refresh" button should trigger a backend process and update the displayed topics.

### Implementation for User Story 3

- [x] T015 [US3] Implement `POST /scrape` endpoint in `backend/src/api/routes/scraper.py`.
- [x] T016 [US3] Implement web scraping logic in `backend/src/services/scraper_service.py`.
- [x] T017 [US3] Implement topic identification logic in `backend/src/services/scraper_service.py`.
- [x] T018 [US3] Implement summarization logic using LLMs in `backend/src/services/summarizer_service.py`.
- [x] T019 [P] [US3] Add a "Refresh" button to the `HomeComponent` template in `frontend/src/app/components/home/home.component.html`.
- [x] T020 [US3] Implement the click handler for the "Refresh" button in `HomeComponent`.

---

## Phase 5: User Story 2 - Switch LLM Provider (Priority: P2)

**Goal**: Allow the user to switch the LLM provider for summarization.

**Independent Test**: Changing the LLM provider in the UI should be reflected in subsequent summaries.

### Implementation for User Story 2

- [x] T021 [US2] Implement `GET /config` and `POST /config` endpoints in `backend/src/api/routes/config.py`.
- [x] T022 [US2] Implement service logic for managing configuration in `backend/src/services/config_service.py`.
- [x] T023 [P] [US2] Create `ConfigSelectorComponent` in `frontend/src/app/components/config-selector/config-selector.component.ts`.
- [x] T024 [US2] Add `ConfigSelectorComponent` to the `HomeComponent` template.
- [x] T025 [US2] Implement state management for the LLM provider selection using an Angular service.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T026 [P] Add loading indicators to the frontend for API calls.
- [x] T027 [P] Add basic error handling and display to the frontend.
- [x] T028 [P] Add structured logging to the backend.
- [x] T029 Review and finalize `quickstart.md` with complete instructions.

---

## Dependencies & Execution Order

- **User Story 1 (P1)**: Depends on Phase 2.
- **User Story 3 (P1)**: Depends on Phase 2.
- **User Story 2 (P2)**: Depends on Phase 2.

All user stories can be worked on in parallel after Phase 2 is complete.
