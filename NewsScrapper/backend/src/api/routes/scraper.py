from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services import scraper_service, summarizer_service
from src.database import get_db, Base, engine
import logging
from src.models import models

router = APIRouter()

@router.post("/scrape")
def scrape_and_summarize(db: Session = Depends(get_db)):
    logging.info("Scrape and summarize process started.")
    try:
        # --- Database Cleanup ---
        print("Dropping all database tables...")
        Base.metadata.drop_all(bind=engine)
        print("Database tables dropped.")

        print("Creating all database tables...")
        Base.metadata.create_all(bind=engine)
        print("Database tables created.")
        # --- End Database Cleanup ---

        articles = scraper_service.scrape_google_news()
        trending_topics = scraper_service.get_topics_from_articles(articles)
        scraper_service.save_articles_and_topics(db, articles, trending_topics)
        summarizer_service.summarize_topics(db)
        logging.info("Scrape and summarize process completed.")
        return {"message": "Scraping and summarization complete."}
    except Exception as e:
        logging.error(f"Error during scrape and summarize process: {e}")
        raise HTTPException(status_code=500, detail=str(e))
