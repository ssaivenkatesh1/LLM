# Data Model

This document describes the conceptual data models for the Document Summarization Tool. As there is no data persistence, these models represent the in-memory data structures used during a single API request.

## 1. Document

Represents the file uploaded by the user.

- **Type**: In-memory object
- **Source**: PDF file upload

| Field | Type | Description |
|---|---|---|
| `filename` | string | The original name of the uploaded file (e.g., `report.pdf`). |
| `content` | string | The full text extracted from the PDF. |
| `size` | integer | The size of the file in bytes. |

## 2. Summary

Represents the generated summary text.

- **Type**: In-memory object
- **Source**: Output from the summarization model

| Field | Type | Description |
|---|---|---|
| `original_word_count` | integer | The word count of the original extracted text. |
| `summary_text` | string | The generated summary. |
| `summary_word_count` | integer | The word count of the summary text. |

## Relationships

A `Summary` is generated from one `Document`. There is a one-to-one relationship between a document processed in a request and the summary returned.
