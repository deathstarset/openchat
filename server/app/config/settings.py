from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

env = os.getenv("ENV", "local")
if env == "docker":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.local")


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
    OLLAMA_URL: str = os.getenv("LLM_URL") or ""


settings = Settings()
