from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database_base import Base
import datetime

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    source = Column(String)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    topics = relationship("Topic", secondary="article_topic_link", back_populates="articles")

class Topic(Base):

    __tablename__ = "topics"



    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, index=True)



    articles = relationship("NewsArticle", secondary="article_topic_link", back_populates="topics")
    summary = relationship("Summary", back_populates="topic", uselist=False)

class ArticleTopicLink(Base):
    __tablename__ = "article_topic_link"
    article_id = Column(Integer, ForeignKey("news_articles.id"), primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id"), primary_key=True)

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    text = Column(String)
    llm_provider = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    topic = relationship("Topic", back_populates="summary")
