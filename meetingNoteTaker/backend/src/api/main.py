from fastapi import FastAPI, File, UploadFile
from src.services.transcription import transcribe_audio
from src.services.summarization import summarize_text
from src.services.task_extraction import extract_tasks
from src.lib.database import setup_database
import sqlite3
import tempfile

app = FastAPI()

@app.on_event("startup")
def startup_event():
    setup_database()

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    transcribed_text = transcribe_audio(tmp_path)
    structured_note = summarize_text(transcribed_text)
    tasks = extract_tasks(transcribed_text)
    print("structured_note = ", structured_note, "tasks = ", tasks)
    conn = sqlite3.connect('meeting_notes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO StructuredNote (content) VALUES (?)", (structured_note,))
    note_id = cursor.lastrowid
    for task in tasks.split('\n'):
        if task.strip():
            cursor.execute("INSERT INTO Task (structured_note_id, description) VALUES (?, ?)", (note_id, task.strip()))
    conn.commit()
    conn.close()

    return {"structured_note": structured_note, "tasks": tasks}