from sqlalchemy import DateTime
from .messages import Message
from app.db.base import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime


class Conversation(Base):
    __tablename__ = "conversations"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    messages = relationship("Message", back_populates="conversation")
    created_at = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
