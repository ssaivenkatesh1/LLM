# Data Model

## User
*   `id`: INTEGER (Primary Key)
*   `username`: TEXT (Unique)
*   `created_at`: TIMESTAMP

## AudioRecording
*   `id`: INTEGER (Primary Key)
*   `user_id`: INTEGER (Foreign Key to User)
*   `file_path`: TEXT
*   `file_size`: INTEGER
*   `duration`: INTEGER
*   `status`: TEXT (e.g., "processing", "completed", "error")
*   `created_at`: TIMESTAMP

## StructuredNote
*   `id`: INTEGER (Primary Key)
*   `audio_recording_id`: INTEGER (Foreign Key to AudioRecording)
*   `content`: TEXT
*   `created_at`: TIMESTAMP
*   `updated_at`: TIMESTAMP

## Task
*   `id`: INTEGER (Primary Key)
*   `structured_note_id`: INTEGER (Foreign Key to StructuredNote)
*   `description`: TEXT
*   `assignee`: TEXT (Optional)
*   `due_date`: DATE (Optional)
*   `is_completed`: BOOLEAN
*   `created_at`: TIMESTAMP
*   `updated_at`: TIMESTAMP
