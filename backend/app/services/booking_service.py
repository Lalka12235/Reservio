from fastapi import HTTPException,status
from datetime import datetime

from app.repositories.booking_repo import BookingRepository

from app.services.user_service import UserServices
from app.services.room_service import RoomService
from app.services.hotel_service import HotelService

from app.schemas.booking_schema import BookingSchema



class BookingService:

    @staticmethod
    def get_booking_by_user(username: str):
        user = UserServices.get_user(username)

        result = BookingRepository.get_booking_by_user(user.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Not booking found'
            )
        
        return {'message': 'success','result': result}
    

    @staticmethod
    def get_all_booking_by_user(username: str):
        user = UserServices.get_user(username)

        result = BookingRepository.get_all_booking_by_user(user.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Not booking found'
            )
        
        return {'message': 'success','bookings': {[booking for booking in result]}}
    

    @staticmethod
    def create_booking(booking: BookingSchema,title_hotel: str, title_room: str, username: str):
        user = UserServices.get_user(username)

        hotel = HotelService.get_hotel_by_title(title_hotel)

        room = RoomService.get_room_by_title(title_hotel,title_room)

        result = BookingRepository.create_booking(booking,hotel.id,room.id,user.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not create'
            )
        
        return {'message': 'success','create': result}
    

    @staticmethod
    def delete_booking(username: str):
        user = UserServices.get_user(username)

        result = BookingRepository.delete_booking(user.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not delete'
            )
        return {'message': 'success','delete': result}
        