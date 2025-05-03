from fastapi import APIRouter

from app.services.hotel_service import HotelService
from app.schemas.hotel_schema import HotelSchema


hotel = APIRouter(
    tags=['Hotel']
)



@hotel.get('/api/v1/hotels/{title}')
async def get_hotel_by_Title(title: str):
    return HotelService.get_hotel_by_title(title)


@hotel.post('/api/v1/hotels/')
async def create_info_about_hotel(hotel_data: HotelSchema):
    return HotelService.create_info_about_hotel(hotel_data)


@hotel.put('/api/v1/hotels/{old_title}')
async def update_info_about_hotel(old_title: str, hotel_data: HotelSchema):
    return HotelService.update_info_about_hotel(old_title,hotel_data)


@hotel.delete('/api/v1/hotels/{title}')
async def delete_hotel(title: str):
    return HotelService.delete_hotel(title)