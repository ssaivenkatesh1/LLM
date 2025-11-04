from sqlalchemy.orm import Session, joinedload
from ..models import models

def get_topics_with_summaries(db: Session, skip: int = 0, limit: int = 100):
    topics = db.query(models.Topic).options(joinedload(models.Topic.summary)).offset(skip).limit(limit).all()
    
    result = []
    for topic in topics:
        summary_text = topic.summary.text if topic.summary else ""
        article = db.query(models.NewsArticle).filter(models.NewsArticle.title == topic.name).first()
        url = article.url if article else ""
        result.append({
            "id": topic.id,
            "name": topic.name,
            "summary": summary_text,
            "url": url
        })
    return result
