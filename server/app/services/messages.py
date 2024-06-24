from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.messages import Message
from sqlalchemy.future import select
from app.schemas.messages import CreateMessage
from fastapi import HTTPException


async def add_message(create_message: CreateMessage, db: AsyncSession):
    new_message = Message(
        conversation_id=create_message.conversation_id,
        sender=create_message.sender,
        content=create_message.content,
    )
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message


async def find_message_by_id(id: str, db: AsyncSession):
    result = await db.execute(select(Message).filter(Message.id == id))
    message = result.scalars().first()
    if message is None:
        raise HTTPException(status_code=404, detail="Message Not Found")
    return message


async def find_messages(db: AsyncSession):
    result = await db.execute(select(Message))
    messages = result.scalars().all()
    return messages


async def remove_message(id: str, db: AsyncSession):
    message = await find_message_by_id(id, db)
    await db.delete(message)
    await db.commit()