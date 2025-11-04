import requests

class ChatLLM:
    """
    Handles interaction with the local LLM server (Ollama).
    """

    def __init__(self, model_name="llama3.2", host="http://host.docker.internal:11434"):
        """
        Initialize the LLM client.

        :param model_name: Name of the model to use with Ollama.
        :param host: Base URL of the Ollama server.
        """
        self.model_name = model_name
        self.base_url = f"{host}/api/generate"

    def generate_response(self, prompt: str) -> str:
        """
        Send a prompt to the LLM and return its response.

        :param prompt: The user input to send to the model.
        :return: The model's generated response as a string.
        """

        payload = {"model": self.model_name, "prompt": prompt, "stream": False}
        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()
        return response.json()["response"]


