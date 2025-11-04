# Research & Decisions

This document records the technical decisions made during the planning phase for the Global News Topic Tracker.

## Backend Technology Stack

-   **Decision**:
    -   **Language**: Python 3.11+
    -   **API Framework**: FastAPI
    -   **Scraping**: BeautifulSoup4 with the `requests` library.
    -   **Database ORM**: SQLAlchemy with SQLite.
    -   **LLM SDKs**: `google-generativeai` and `openai`.
-   **Rationale**:
    -   **FastAPI** was chosen for its high performance, asynchronous support (which is beneficial for I/O-bound tasks like scraping and calling LLM APIs), and automatic generation of OpenAPI documentation.
    -   **BeautifulSoup** is a robust and widely-used library for web scraping, making it a reliable choice.
    -   **SQLAlchemy** provides a powerful ORM that abstracts away the database, and **SQLite** is a simple, file-based database perfect for the scale of this project.
-   **Alternatives considered**:
    -   **Flask**: A solid choice, but FastAPI's async capabilities and data validation with Pydantic are better suited for this project.
    -   **Scrapy**: A more powerful scraping framework, but it's overkill for scraping a single, well-structured site like Google News.

## Frontend Technology Stack

-   **Decision**:
    -   **Framework**: Angular
    -   **Language**: TypeScript
    -   **API Client**: Angular HttpClient
-   **Rationale**:
    -   **Angular** is a comprehensive framework that provides a structured architecture, which is beneficial for long-term maintenance.
    -   **TypeScript** provides static typing, which helps to catch errors early.
    -   **Angular HttpClient** is a built-in module for making HTTP requests.
-   **Alternatives considered**:
    -   **React**: A popular library, but Angular's full-featured framework is a better fit for this project's structure.
    -   **Vue.js**: Another excellent framework, but Angular's strong opinions on structure are a good fit here.

## Deployment

-   **Decision**: The initial plan will focus on local development. A `quickstart.md` will be provided. Deployment to a cloud provider can be a future task.
-   **Rationale**: This allows for rapid iteration and development without the overhead of setting up cloud infrastructure.

## Containerization

-   **Decision**: Docker will be used to containerize both the frontend and backend applications. `docker-compose` will be used for local orchestration.
-   **Rationale**: Docker provides a consistent and reproducible environment for development, testing, and deployment. `docker-compose` simplifies the management of multi-container applications.
-   **Alternatives considered**: Podman, but Docker has a larger community and more extensive tooling.
