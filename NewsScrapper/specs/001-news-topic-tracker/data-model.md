# Data Model

This document defines the data structures for the Global News Topic Tracker. The model is designed to be implemented using SQLAlchemy with a relational database like SQLite.

## Entities

### 1. NewsArticle

Represents a single news article scraped from a source.

-   **`id`**: Integer, Primary Key
-   **`title`**: String, Not Nullable
-   **`url`**: String, Not Nullable, Unique
-   **`source`**: String, Not Nullable
-   **`scraped_at`**: DateTime, Not Nullable, Default: current timestamp

### 2. Topic

Represents a trending topic identified from keywords in article titles.

-   **`id`**: Integer, Primary Key
-   **`name`**: String, Not Nullable, Unique

### 3. ArticleTopicLink

A many-to-many link table between articles and topics.

-   **`article_id`**: Integer, Foreign Key to `NewsArticle.id`
-   **`topic_id`**: Integer, Foreign Key to `Topic.id`

### 4. Summary

Stores the generated summary for a given topic.

-   **`id`**: Integer, Primary Key
-   **`topic_id`**: Integer, Foreign Key to `Topic.id`
-   **`text`**: String, Not Nullable
-   **`llm_provider`**: String, Not Nullable (e.g., "gemini" or "openai")
-   **`created_at`**: DateTime, Not Nullable, Default: current timestamp

## Relationships

-   A `NewsArticle` can be associated with multiple `Topic`s.
-   A `Topic` can be associated with multiple `NewsArticle`s.
-   A `Topic` can have multiple `Summary`s (generated at different times or with different providers).
