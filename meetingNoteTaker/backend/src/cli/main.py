import argparse
import sqlite3
import subprocess
import tempfile
import os
import logging
from tqdm import tqdm
from src.services.transcription import transcribe_audio
from src.services.summarization import summarize_text
from src.services.task_extraction import extract_tasks
from src.lib.database import setup_database

def main():
    parser = argparse.ArgumentParser(description='Meeting Note Taker')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    subparsers = parser.add_subparsers(dest='command')

    # process-audio command
    process_audio_parser = subparsers.add_parser('process-audio', help='Process a meeting audio file')
    process_audio_parser.add_argument('file_path', type=str, help='The path to the audio file to process')
    process_audio_parser.add_argument('--output-dir', type=str, default='.', help='The directory to save the generated notes and task list to')

    # list-notes command
    list_notes_parser = subparsers.add_parser('list-notes', help='List all generated structured notes')

    # show-note command
    show_note_parser = subparsers.add_parser('show-note', help='Show the content of a specific structured note')
    show_note_parser.add_argument('note_id', type=int, help='The ID of the note to show')

    # edit-note command
    edit_note_parser = subparsers.add_parser('edit-note', help='Opens a specific structured note in the default text editor for editing')
    edit_note_parser.add_argument('note_id', type=int, help='The ID of the note to edit')

    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    # Setup database
    try:
        logging.info("Setting up database...")
        setup_database()
        logging.info("Database setup complete.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return

    if args.command == 'process-audio':
        try:
            with tqdm(total=4, desc="Processing Audio") as pbar:
                logging.info(f"Processing audio file: {args.file_path}")
                pbar.set_description("Transcribing audio")
                transcribed_text = transcribe_audio(args.file_path)
                pbar.update(1)

                pbar.set_description("Summarizing text")
                structured_note = summarize_text(transcribed_text)
                pbar.update(1)

                pbar.set_description("Extracting tasks")
                tasks = extract_tasks(transcribed_text)
                pbar.update(1)

                pbar.set_description("Saving to database")
                conn = sqlite3.connect('meeting_notes.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO StructuredNote (content) VALUES (?)", (structured_note,))
                note_id = cursor.lastrowid
                for task in tasks.split('\n'):
                    if task.strip():
                        cursor.execute("INSERT INTO Task (structured_note_id, description) VALUES (?, ?)", (note_id, task.strip()))
                conn.commit()
                conn.close()
                pbar.update(1)
            logging.info("Structured Note and Tasks saved to database.")
        except FileNotFoundError:
            logging.error(f"Error: The file {args.file_path} was not found.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
    elif args.command == 'list-notes':
        try:
            logging.info("Listing all notes...")
            conn = sqlite3.connect('meeting_notes.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, content FROM StructuredNote")
            notes = cursor.fetchall()
            conn.close()
            for note in notes:
                print(f"Note ID: {note[0]}")
                print(f"Content: {note[1]}")
                print("-" * 20)
            logging.info(f"{len(notes)} notes found.")
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
    elif args.command == 'show-note':
        try:
            logging.info(f"Showing note with ID: {args.note_id}")
            conn = sqlite3.connect('meeting_notes.db')
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM StructuredNote WHERE id = ?", (args.note_id,))
            note = cursor.fetchone()
            conn.close()
            if note:
                print(note[0])
            else:
                logging.warning(f"Note with ID {args.note_id} not found.")
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
    elif args.command == 'edit-note':
        try:
            logging.info(f"Editing note with ID: {args.note_id}")
            conn = sqlite3.connect('meeting_notes.db')
            cursor = conn.cursor()
            cursor.execute("SELECT content FROM StructuredNote WHERE id = ?", (args.note_id,))
            note = cursor.fetchone()
            if note:
                with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as tmpfile:
                    tmpfile.write(note[0])
                    tmpfile.flush()
                    editor = os.getenv('EDITOR', 'vim') # or notepad on windows
                    subprocess.call([editor, tmpfile.name])
                    tmpfile.seek(0)
                    updated_content = tmpfile.read()
                cursor.execute("UPDATE StructuredNote SET content = ? WHERE id = ?", (updated_content, args.note_id))
                conn.commit()
                logging.info(f"Note {args.note_id} updated.")
            else:
                logging.warning(f"Note with ID {args.note_id} not found.")
            conn.close()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
