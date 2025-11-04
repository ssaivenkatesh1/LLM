from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.services import topic_service
from src.database import get_db
from src.services import scraper_service

router = APIRouter()
@router.get("/topics")
def read_topics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    topics = topic_service.get_topics_with_summaries(db, skip=skip, limit=limit)
    print("Topics ==== ", topics)
    #scraper_service.google_parse()
    return topics
