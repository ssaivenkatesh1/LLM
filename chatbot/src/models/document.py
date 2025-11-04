from pydantic import BaseModel
from typing import Literal

class Document(BaseModel):
    file_name: str
    content: str
    status: Literal["uploaded", "processing", "ready", "error"]
