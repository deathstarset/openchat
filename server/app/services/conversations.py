from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.conversations import Conversation
from sqlalchemy.future import select
from fastapi import HTTPException


async def add_conversation(db: AsyncSession):
    new_conversation = Conversation()
    db.add(new_conversation)
    await db.commit()
    await db.refresh(new_conversation)
    return new_conversation


async def find_conversation_by_id(id: str, db: AsyncSession):
    result = await db.execute(select(Conversation).filter(Conversation.id == id))
    conversation = result.scalars().first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation Not Found")
    return conversation


async def remove_conversation(id: str, db: AsyncSession):
    conversation = await find_conversation_by_id(id, db)
    await db.delete(conversation)
    await db.commit()


async def find_conversations(db: AsyncSession):
    result = await db.execute(select(Conversation))
    conversations = result.scalars().all()
    return conversations
