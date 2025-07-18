from fastapi import APIRouter,Depends
from app.config.session import get_db
from typing import Annotated
from sqlalchemy.orm import Session

from app.services.booking_service import BookingService
from app.schemas.booking_schema import BookingSchema

booking = APIRouter(
    prefix='/api/v1/users/{username}/bookings',
    tags=['Booking'],
)

db_dependency = Annotated[Session,Depends(get_db)]


@booking.get('/{booking_id}')
async def get_booking(db:db_dependency,username: str):
    return BookingService.get_booking_by_user(db,username)


@booking.get('/')
async def get_all_booking(db:db_dependency,username: str, skip: int = 0, limit: int = 10):
    return BookingService.get_all_booking_by_user(db,username,skip,limit)


@booking.post('/')
async def create_booking(db:db_dependency,booking: BookingSchema,title_hotel: str, title_room: str, username: str):
    return BookingService.create_booking(db,booking,title_hotel,title_room,username)


@booking.delete('/')
async def delete_booking(db:db_dependency,username: str):
    return BookingService.delete_booking(db,username)

