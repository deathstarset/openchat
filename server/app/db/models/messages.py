from sqlalchemy import DateTime, ForeignKey, Text, Enum
from app.db.base import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import enum


class SenderEnum(str, enum.Enum):
    user = "user"
    bot = "bot"


class Message(Base):
    __tablename__ = "messages"
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = mapped_column(UUID(as_uuid=True), ForeignKey("conversations.id"))
    conversation = relationship("Conversation", back_populates="messages")
    sender = mapped_column(Enum(SenderEnum), nullable=False)
    content = mapped_column(Text)
    created_at = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
