from fastapi import APIRouter,Depends
from app.config.session import get_db
from typing import Annotated
from sqlalchemy.orm import Session

from app.services.room_category_service import RoomCategoryService
from app.schemas.room_category_schema import RoomCategorySchema

room_category = APIRouter(
    prefix="/api/v1/hotels/{hotel_title}/room-categories",
    tags=['Room Categories']
)

db_dependency = Annotated[Session,Depends(get_db)]

@room_category.get('/')
async def get_all_room_category(db:db_dependency,title_hotel: str):
    return RoomCategoryService.get_all_room_category_by_hotel(db,title_hotel)


@room_category.get('/{title_hotel}')
async def get_room_category(db:db_dependency,title_hotel: str, title_category: str):
    return RoomCategoryService.get_room_category_by_title(db,title_hotel,title_category)


@room_category.post('/')
async def create_room_category(db:db_dependency,title_hotel: str, category: RoomCategorySchema):
    return RoomCategoryService.create_room_category(db,title_hotel,category)


@room_category.put('/{title_hotel}')
async def update_room_category(db:db_dependency,title_hotel: str, category: RoomCategorySchema):
    return RoomCategoryService.create_room_category(db,title_hotel,category)


@room_category.delete('/{title_hotel}')
async def delete_room_category(db:db_dependency,title_hotel: str, title_category: str):
    return RoomCategoryService.delete_room_category(db,title_hotel,title_category)