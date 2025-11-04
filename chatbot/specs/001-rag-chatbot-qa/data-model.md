# Data Model

This document describes the data model for the RAG-based chatbot.

## Entities

### Document
Represents a file uploaded by any user into the shared pool.

-   **file_name**: `string` - The name of the uploaded file.
-   **content**: `string` - The extracted text content of the document.
-   **status**: `string` - The processing status of the document. Can be one of: `uploaded`, `processing`, `ready`, `error`.

### Embedding
Represents a vector embedding of a chunk of text from a document. This will be stored in ChromaDB.

-   **id**: `string` - A unique identifier for the embedding.
-   **document_id**: `string` - The ID of the document this embedding belongs to.
-   **text_chunk**: `string` - The chunk of text that the embedding represents.
-   **vector**: `array` - The vector embedding.

### Question
Represents a user's query.

-   **text**: `string` - The text of the question.

### Answer
Represents the system's response to a question.

-   **text**: `string` - The text of the answer.
-   **source_documents**: `array` - A list of document chunks that were used to generate the answer.
