# Chatbot Constitution

## Core Principles

### I. Frontend - Simple Chat UI
A clean, user-friendly interface is paramount. The UI should be intuitive and focus on the conversation.

### II. Backend - FastAPI
A lightweight and performant backend is essential for a responsive chat experience.

### III. Stateless Interaction
The backend will be stateless, simplifying the architecture and scaling. The UI will hold the conversation state.

### IV. Clear API Contract
A well-defined API contract between the UI and the backend is crucial for independent development and testing.

### V. Testability
Both frontend and backend components should be designed with testability in mind.

## Technical Specifications

### Frontend
- Must display conversation history.
- Must have a text input for user messages.
- Must have a send button.

### Backend (FastAPI)
- Must have a single endpoint `/chat` that accepts POST requests.
- The request body should be a JSON object with a `message` field.
- The response should be a JSON object with a `reply` field.

## Governance

This constitution is the single source of truth for the project's technical direction. Any changes must be proposed and agreed upon by the team.

**Version**: 1.0.0 | **Ratified**: 2025-11-01 | **Last Amended**: 2025-11-01