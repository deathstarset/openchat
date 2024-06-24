from pydantic import BaseModel, validator
from app.db.models.messages import SenderEnum
from uuid import UUID


class CreateMessage(BaseModel):
    conversation_id: str
    sender: SenderEnum
    content: str

    @validator("conversation_id")
    def validate_uuid(cls, v):
        try:
            UUID(v, version=4)
        except ValueError:
            raise ValueError("Invalid UUID format")
        return v
