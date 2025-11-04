# LLM Chat Application

This is a simple chat application that uses a local LLM to generate responses.

## How to start the application

To start the application, run the following command:

```
docker-compose up -d
```

This will start the following services:

* `backend`: The FastAPI backend service, running on port 8020.
* `frontend`: The Streamlit frontend service, running on port 8521. You can access the chat application at `http://localhost:8521`.

## How to stop the application

To stop the application, run the following command:

```
docker-compose down
```
