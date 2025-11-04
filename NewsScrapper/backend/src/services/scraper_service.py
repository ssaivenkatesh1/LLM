import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from sqlalchemy.orm import Session
from ..models import models
import datetime
from dateutil.parser import parse


import feedparser
#from transformers import pipeline
from src.services import summarizer_service

def scrape_google_news():
    url = "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-IN&gl=IN&ceid=IN:en"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")

    articles = []
    for item in items:
        title = item.title.text
        link = item.link.text
        source_tag = item.source.text if item.source else "Unknown"
        pub_date = item.pubDate.text if item.pubDate else ""

        articles.append({
            "title": title,
            "url": link,
            "source": source_tag,
            "published_at": parse(pub_date) if pub_date else datetime.datetime.utcnow()
        })

    # for article in articles:
    #     print("Title = ", article["title"])

    print(f"✅ Fetched {len(articles)} articles")
    return articles

def get_topics_from_articles(articles: list[dict]) -> list[str]:
    return [article['title'] for article in articles[:10]]

def save_articles_and_topics(db: Session, articles: list[dict], trending_topics: list[str]):
    for article_data in articles:
        print("save_articles_and_topics::Article_URL", article_data['url'])
        existing_article = db.query(models.NewsArticle).filter_by(url=article_data['url']).first()
        if not existing_article:
            article = models.NewsArticle(**article_data)
            db.add(article)
            db.commit()
            db.refresh(article)
        else:
            article = existing_article

        for topic_name in trending_topics:
            topic = db.query(models.Topic).filter_by(name=topic_name).first()
            if not topic:
                topic = models.Topic(name=topic_name)
                db.add(topic)
                db.commit()
                db.refresh(topic)

            link = db.query(models.ArticleTopicLink).filter_by(article_id=article.id, topic_id=topic.id).first()
            if not link:
                link = models.ArticleTopicLink(article_id=article.id, topic_id=topic.id)
                db.add(link)
                db.commit()
                db.refresh(link)



def google_parse():
    # Step 1: Parse Google News RSS feed
    query = "AI"
    feed_url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(feed_url)

    print("111111")
    # Step 2: Extract news items
    articles = []
    for entry in feed.entries[:5]:  # Limit to top 5
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary if hasattr(entry, 'summary') else ""
        })

    # Step 3: Summarize the news using a Hugging Face model
    #summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("2222222")
    for article in articles:
        print("📰", article["title"])
        print("3333333")
        print("Article", article)
        summary = summarizer_service.summarize_text_with_gemini(article["title"])
        print("4444")
        print("Summary", summary)
        #summary = summarizer(article["summary"] or article["title"], max_length=60, min_length=20, do_sample=False)
        #print("👉 Summary:", summary[0]['summary_text'])
        #print("🔗 Link:", article["link"])
        print("-" * 80)
