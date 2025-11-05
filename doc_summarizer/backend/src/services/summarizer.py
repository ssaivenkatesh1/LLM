from transformers import pipeline

class Summarizer:
    def __init__(self):
        """Initializes the Summarizer by loading the BART large CNN model."""
        # Load the summarization model. This will download the model the first time.
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.max_chunk_length = 1024 # BART's maximum input length

    def _chunk_text(self, text: str) -> list[str]:
        """Splits the input text into chunks that fit the model's maximum input length.

        Args:
            text (str): The input text to be chunked.

        Returns:
            list[str]: A list of text chunks.
        """
        # Simple chunking strategy: split by sentences and then group them
        # This is a basic implementation and can be improved.
        sentences = text.split('. ')
        chunks = []
        current_chunk = ""
        for sentence in sentences:
            if len(current_chunk) + len(sentence) + 2 <= self.max_chunk_length:
                current_chunk += sentence + ". "
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    def summarize(self, text: str, min_length: int = 30, max_length: int = 150) -> str:
        """Generates a summary for the given text, handling chunking if necessary.

        Args:
            text (str): The input text to be summarized.
            min_length (int): The minimum length of the generated summary.
            max_length (int): The maximum length of the generated summary.

        Returns:
            str: The generated summary text.
        """
        if not text.strip():
            return ""

        # If text is too long, chunk it and summarize each chunk, then combine.
        if len(text) > self.max_chunk_length:
            chunks = self._chunk_text(text)
            summaries = []
            for chunk in chunks:
                if chunk:
                    # Adjust max_length for chunks to avoid very long intermediate summaries
                    chunk_summary = self.summarizer(chunk, min_length=min_length // len(chunks) or 10, max_length=max_length // len(chunks) or 50, do_sample=False)
                    summaries.append(chunk_summary[0]["summary_text"])
            return " ".join(summaries)
        else:
            summary = self.summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
            return summary[0]["summary_text"]
