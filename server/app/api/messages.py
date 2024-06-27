from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies.db_session import get_db
from app.services.messages import (
    find_message_by_id,
    find_messages,
    remove_message,
    add_message,
    find_message_by_convo_id,
)
from fastapi import APIRouter, Depends, Query
from app.schemas.messages import CreateMessage
from typing import Optional
from uuid import UUID

router = APIRouter()


@router.post("")
async def create_message(
    create_message_data: CreateMessage, db: AsyncSession = Depends(get_db)
):
    message = await add_message(create_message_data, db)
    return {"message": message}


@router.get("")
async def get_messages(
    convo_id: Optional[UUID] = Query(None), db: AsyncSession = Depends(get_db)
):
    if convo_id is None:
        messages = await find_messages(db)
    else:
        messages = await find_message_by_convo_id(convo_id, db)
    return {"messages": messages}


@router.get("/{id}")
async def get_message(id: str, db: AsyncSession = Depends(get_db)):
    message = await find_message_by_id(id, db)
    return {"message": message}


@router.delete("/{id}")
async def delete_message(id: str, db: AsyncSession = Depends(get_db)):
    await remove_message(id, db)
    return {"message": "Message Deleted Succefully"}
