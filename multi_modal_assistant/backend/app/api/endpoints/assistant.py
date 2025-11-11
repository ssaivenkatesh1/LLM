import logging
from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from typing import Optional
from app.services.model_service import model_service

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/query")
async def query_assistant(
    query: str = Form(""),
    image: Optional[UploadFile] = File(None),
):
    """
    Receives a query and an optional image, and returns a response from the assistant.
    """
    logger.info(f"Query endpoint called with query: '{query}' and image: {image.filename if image else 'None'}")
    image_data = None
    if image:
        if not image.content_type.startswith("image/"):
            logger.warning(f"Invalid file type uploaded: {image.content_type}")
            raise HTTPException(status_code=400, detail="File provided is not an image.")
        image_data = await image.read()
        logger.info(f"Read image data of size: {len(image_data)} bytes")

    if not query and not image_data:
        logger.warning("Query attempted with no query or image.")
        raise HTTPException(status_code=400, detail="Please provide a query or an image.")

    try:
        result = model_service.predict(query=query, image_data=image_data)
        if "error" in result:
            logger.error(f"Prediction failed: {result.get('details')}")
        else:
            logger.info("Prediction successful.")
        print("Result:", result)
        return result
    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
