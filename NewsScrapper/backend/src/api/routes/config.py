from fastapi import APIRouter
from pydantic import BaseModel
from src.services import config_service
import logging

router = APIRouter()

class Config(BaseModel):
    llm_provider: str

@router.get("/config")
def read_config():
    logging.info("Reading config.")
    return config_service.get_config()

@router.post("/config")
def update_config(config: Config):
    logging.info(f"Updating config with: {config.dict()}")
    return config_service.update_config(config.dict())
