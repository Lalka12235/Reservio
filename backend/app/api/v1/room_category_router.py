from fastapi import APIRouter

from app.services.room_category_service import RoomCategoryService
from app.schemas.room_category_schema import RoomCategorySchema

room_category = APIRouter(
    prefix="/api/v1/room-category",
    tags=['Room Category']
)


@room_category.get('/{title_hotel}')
async def get_all_room_category_by_hotel(title_hotel: str):
    return RoomCategoryService.get_all_room_category_by_hotel(title_hotel)


@room_category.get('/{title_hotel}')
async def get_room_category_by_title(title_hotel: str, title_category: str):
    return RoomCategoryService.get_room_category_by_title(title_hotel,title_category)


@room_category.post('/')
async def create_room_category(title_hotel: str, category: RoomCategorySchema):
    return RoomCategoryService.create_room_category(title_hotel,category)


@room_category.put('/{title_hotel}')
async def update_room_category(title_hotel: str, category: RoomCategorySchema):
    return RoomCategoryService.create_room_category(title_hotel,category)


@room_category.delete('/{title_hotel}')
async def delete_room_category(title_hotel: str, title_category: str):
    return RoomCategoryService.delete_room_category(title_hotel,title_category)