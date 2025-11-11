import logging
import base64
import requests
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class ModelService:
    def __init__(self, model_path: str):
        # Use chat endpoint (recommended for moondream)
        self.OLLAMA_URL = "http://host.docker.internal:11434/api/chat"
        self.MODEL_NAME = "moondream"

    def predict(self, query: str, image_data: Optional[bytes] = None) -> Dict[str, Any]:
        logger.info(f"Query: {query}")

        # Construct user message
        message = {"role": "user", "content": query}

        # If image is provided, attach as base64 to message
        if image_data:
            encoded = base64.b64encode(image_data).decode("utf-8")
            message["images"] = [encoded]
            logger.info("Image encoded and attached for model request.")
        else:
            logger.info("No image provided.")

        payload = {
            "model": self.MODEL_NAME,
            "messages": [message],
            "stream": False
        }

        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(self.OLLAMA_URL, json=payload, headers=headers, timeout=600)
            response.raise_for_status()

            data = response.json()
            answer = data.get("message", {}).get("content", "").strip()

            logger.info(f"Model response: {answer}")
            return {"answer": answer}

        except Exception as e:
            logger.error(f"Model prediction failed: {e}", exc_info=True)
            return {"error": "Model call failed.", "details": str(e)}

model_service = ModelService(model_path="placeholder/model.gguf")
