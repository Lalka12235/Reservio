from fastapi import APIRouter

from app.services.room_service import RoomService
from app.schemas.room_schema import RoomSchema


room = APIRouter(
    prefix='/api/v1/hotels/{hotel_title}/rooms',
    tags=['Room']
)


@room.get('/{title_room}')
async def get_room(title_hotel: str,title_room: str):
    return RoomService.get_room_by_title(title_hotel,title_room)


@room.get('/')
async def get_all_room(title_hotel: str):
    return RoomService.get_all_room_by_hotel(title_hotel)


@room.post('/')
async def create_room(room: RoomSchema,title_hotel: str, title_category: str):
    return RoomService.create_room(room,title_hotel,title_category)


@room.put('/{old_title}')
async def update_room(old_title: str,room: RoomSchema,title_category: str):
    return RoomService.update_room(old_title,room,title_category)


@room.delete('/{title_room}')
async def delete_room(title_room: str, title_hotel: str):
    return RoomService.delete_room(title_room,title_hotel)