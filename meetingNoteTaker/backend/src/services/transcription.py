import whisper

def transcribe_audio(file_path):
    """
    Transcribes an audio file using the Whisper model.
    """
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]
