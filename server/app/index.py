from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse
import requests
from fastapi.middleware.cors import CORSMiddleware
from app.api import conversations
from app.api import messages

app = FastAPI()

OLLAMA_BASE = "http://localhost:11434"

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Prompt(BaseModel):
    message: str


app.include_router(conversations.router, prefix="/api/v1/conversations")
app.include_router(messages.router, prefix="/api/v1/messages")


@app.post("/api/v1/generate")
def generate(prompt: Prompt):
    user_message = prompt.message
    data = {"model": "orca-mini:3b", "prompt": user_message}
    response = requests.post(f"{OLLAMA_BASE}/api/generate", json=data, stream=True)
    response.raise_for_status()

    def generator_response():
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    return StreamingResponse(generator_response(), media_type="application/json")
