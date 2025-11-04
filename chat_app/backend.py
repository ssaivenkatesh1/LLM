from fastapi import FastAPI
from pydantic import BaseModel
from llm_client import ChatLLM

# Initialize FastAPI and LLM client
app = FastAPI()
llm = ChatLLM()

# Request schema for chat endpoint
class ChatRequest(BaseModel):
    message: str

# Response schema for chat endpoint
class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    FastAPI POST endpoint that accepts a user message,
    generates a response using the local LLM, and returns it.
    """
    print("Received Prompt ",req)
    reply = llm.generate_response(req.message)
    return ChatResponse(response=reply)
