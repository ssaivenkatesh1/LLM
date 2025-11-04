from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import topics, scraper, config
import logging
from src.database import engine
from src.models import models

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(topics.router)
app.include_router(scraper.router)
app.include_router(config.router)

@app.get("/")
def read_root():
    logging.info("Root endpoint accessed.")
    return {"Hello": "World"}
