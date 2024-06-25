from app.api.dependencies.db_session import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.conversations import (
    add_conversation,
    remove_conversation,
    find_conversation_by_id,
    find_conversations,
)

router = APIRouter()


@router.post("")
async def create_conversation(db: AsyncSession = Depends(get_db)):
    conversation = await add_conversation(db)
    return {"conversation": conversation}


@router.get("")
async def get_conversations(db: AsyncSession = Depends(get_db)):
    conversations = await find_conversations(db)
    return {"conversations": conversations}


@router.get("/{id}")
async def get_conversation(id: str, db: AsyncSession = Depends(get_db)):
    conversation = await find_conversation_by_id(id, db)
    return {"conversation": conversation}


@router.delete("/{id}")
async def delete_conversation(id: str, db: AsyncSession = Depends(get_db)):
    await remove_conversation(id, db)
    return {"message": "conversation delete succefully"}
