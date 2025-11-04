import os
import google.generativeai as genai
import openai
from sqlalchemy.orm import Session, joinedload
from ..models import models
import requests
from bs4 import BeautifulSoup

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
openai.api_key = os.environ["OPENAI_API_KEY"]

def summarize_text_with_gemini(text: str) -> str:
    # for m in genai.list_models():
    #     print(m.name)
    #     if 'generateContent' in m.supported_generation_methods:
    #         print("Supported = ", m.name)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(f"Summarize the following news article in 5 words or less: {text}")
    return response.text

def summarize_text_with_openai(text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following news article in 3 sentences or less: {text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def summarize_topics(db: Session, llm_provider: str = "gemini"):

    topics_without_summaries = db.query(models.Topic).options(joinedload(models.Topic.articles)).filter(models.Topic.summary == None).all()
    for topic in topics_without_summaries:
        if not topic.articles:
            continue
        article_url = topic.articles[0].url

        try:
            headers = {

                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

            }

            response = requests.get(article_url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            for script in soup(["script", "style"]):
                script.extract()

            article_text = soup.get_text()
            lines = (line.strip() for line in article_text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            article_text = '\n'.join(chunk for chunk in chunks if chunk)
            if not article_text:
                continue

            print("Topic Name == ", topic.name)
            if llm_provider == "gemini":
                summary_text = summarize_text_with_gemini(topic.name)
            elif llm_provider == "openai":
                summary_text = summarize_text_with_openai(topic.name)
            else:
                continue

            summary = models.Summary(
                topic_id=topic.id,
                text=summary_text,
                llm_provider=llm_provider
            )



            db.add(summary)

            db.commit()

        except Exception as e:

            print(f"Error summarizing {article_url}: {e}")
