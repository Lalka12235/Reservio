from fastapi import APIRouter,Depends
from app.config.session import get_db
from typing import Annotated
from sqlalchemy.orm import Session

from app.services.room_service import RoomService
from app.schemas.room_schema import RoomSchema


room = APIRouter(
    prefix='/api/v1/hotels/{hotel_title}/rooms',
    tags=['Room']
)

db_dependency = Annotated[Session,Depends(get_db)]

@room.get('/{title_room}')
async def get_room(db:db_dependency,title_hotel: str,title_room: str):
    return RoomService.get_room_by_title(db,title_hotel,title_room)


@room.get('/')
async def get_all_room(db:db_dependency,title_hotel: str):
    return RoomService.get_all_room_by_hotel(db,title_hotel)


@room.post('/')
async def create_room(db:db_dependency,room: RoomSchema,title_hotel: str, title_category: str):
    return RoomService.create_room(db,room,title_hotel,title_category)


@room.put('/{old_title}')
async def update_room(db:db_dependency,old_title: str,room: RoomSchema,title_category: str):
    return RoomService.update_room(db,old_title,room,title_category)


@room.delete('/{title_room}')
async def delete_room(db:db_dependency,title_room: str, title_hotel: str):
    return RoomService.delete_room(db,title_room,title_hotel)