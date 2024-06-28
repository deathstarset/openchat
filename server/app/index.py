from fastapi import FastAPI, Depends
from pydantic import BaseModel
from starlette.responses import StreamingResponse
import requests
from fastapi.middleware.cors import CORSMiddleware
from app.api import conversations
from app.api import messages
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies.db_session import get_db
from sqlalchemy import select
from app.config.settings import settings

app = FastAPI()

OLLAMA_BASE = settings.OLLAMA_URL

origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "http://172.27.0.4:4173/",
]

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


@app.get("/api/v1/check_db")
async def check(db: AsyncSession = Depends(get_db)):
    await db.execute(select(1))
    return {"message": "Database connection successful"}


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
