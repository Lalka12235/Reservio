from fastapi import APIRouter

from app.services.booking_service import BookingService
from app.schemas.booking_schema import BookingSchema

booking = APIRouter(
    prefix='/api/v1/users/{username}/bookings',
    tags=['Booking'],
)


@booking.get('/{booking_id}')
async def get_booking(username: str):
    return BookingService.get_booking_by_user(username)


@booking.get('/')
async def get_all_booking(username: str, skip: int = 0, limit: int = 10):
    return BookingService.get_all_booking_by_user(username,skip,limit)


@booking.post('/')
async def create_booking(booking: BookingSchema,title_hotel: str, title_room: str, username: str):
    return BookingService.create_booking(booking,title_hotel,title_room,username)


@booking.delete('/{username}')
async def delete_booking(username: str):
    return BookingService.delete_booking(username)

