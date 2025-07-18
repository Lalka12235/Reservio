from fastapi import APIRouter,Depends
from app.config.session import get_db
from typing import Annotated
from sqlalchemy.orm import Session

from app.services.hotel_service import HotelService
from app.schemas.hotel_schema import HotelSchema


hotel = APIRouter(
    prefix="/api/v1/hotels",
    tags=['Hotel']
)

db_dependency = Annotated[Session,Depends(get_db)]

@hotel.get('/{title}')
async def get_hotel(db:db_dependency,title: str):
    return HotelService.get_hotel_by_title(db,title)


@hotel.post('/')
async def create_info_about_hotel(db:db_dependency,hotel_data: HotelSchema):
    return HotelService.create_info_about_hotel(db,hotel_data)


@hotel.put('/{old_title}')
async def update_info_about_hotel(db:db_dependency,old_title: str, hotel_data: HotelSchema):
    return HotelService.update_info_about_hotel(db,old_title,hotel_data)


@hotel.delete('/{title}')
async def delete_hotel(db:db_dependency,title: str):
    return HotelService.delete_hotel(db,title)