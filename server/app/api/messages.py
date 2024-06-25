from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies.db_session import get_db
from app.services.messages import (
    find_message_by_id,
    find_messages,
    remove_message,
    add_message,
)
from fastapi import APIRouter, Depends
from app.schemas.messages import CreateMessage

router = APIRouter()


@router.post("")
async def create_message(
    create_message_data: CreateMessage, db: AsyncSession = Depends(get_db)
):
    message = await add_message(create_message_data, db)
    return {"message": message}


@router.get("")
async def get_messages(db: AsyncSession = Depends(get_db)):
    messages = await find_messages(db)
    return {"messages": messages}


@router.get("/{id}")
async def get_message(id: str, db: AsyncSession = Depends(get_db)):
    message = await find_message_by_id(id, db)
    return {"message": message}


@router.delete("/{id}")
async def delete_message(id: str, db: AsyncSession = Depends(get_db)):
    await remove_message(id, db)
    return {"message": "Message Deleted Succefully"}
