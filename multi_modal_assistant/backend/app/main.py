import logging
from fastapi import FastAPI
from app.api.endpoints import assistant

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)



logger.info("Starting Multimodal Assistant API...")

app.include_router(assistant.router, prefix="/api")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Shutting down Multimodal Assistant API.")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to the Multimodal Assistant API"}
