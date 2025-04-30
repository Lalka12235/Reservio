from fastapi import HTTPException, status
from datetime import datetime

from app.repositories.booking_repo import BookingRepository
from app.services.user_service import UserServices
from app.services.room_service import RoomService
from app.services.hotel_service import HotelService
from app.schemas.booking_schema import BookingSchema


class BookingService:

    @staticmethod
    def _check_booking_dates(booking: BookingSchema):
        if booking.start_date >= booking.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Дата окончания должна быть позже даты начала"
            )
        
        if booking.start_date < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нельзя бронировать на прошедшую дату"
            )

    @staticmethod
    def _check_room_availability(room_id: int, booking: BookingSchema):
        conflicting_bookings = BookingRepository.get_conflicting_bookings(
            room_id=room_id,
            start_date=booking.start_date,
            end_date=booking.end_date
        )
        
        if conflicting_bookings:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Номер уже забронирован на указанные даты"
            )

    @staticmethod
    def get_booking_by_user(username: str):
        user = UserServices.get_user(username)
        result = BookingRepository.get_booking_by_user(user.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Бронирования не найдены'
            )
        
        return {'message': 'success', 'result': result}

    @staticmethod
    def get_all_booking_by_user(username: str, skip: int = 0, limit: int = 10):
        user = UserServices.get_user(username)
        result = BookingRepository.get_all_booking_by_user(user.id, skip, limit)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Бронирования не найдены'
            )
        
        return {
            'message': 'success',
            'bookings': [booking for booking in result],
            'pagination': {
                'skip': skip,
                'limit': limit,
                'total': BookingRepository.get_count_bookings_by_user(user.id)
            }
        }

    @staticmethod
    def create_booking(booking: BookingSchema, title_hotel: str, title_room: str, username: str):
        user = UserServices.get_user(username)
        hotel = HotelService.get_hotel_by_title(title_hotel)
        room = RoomService.get_room_by_title(title_hotel, title_room)

        BookingService._check_booking_dates(booking.start_date, booking.end_date)
        BookingService._check_room_availability(room.id, booking.start_date, booking.end_date)

        try:
            result = BookingRepository.create_booking(
                booking=booking,
                hotel_id=hotel.id,
                room_id=room.id,
                user_id=user.id
            )
            
            return {
                'message': 'Бронирование успешно создано',
                'booking_id': result.id,
                'details': {
                    'hotel': hotel.title,
                    'room': room.title,
                    'dates': f"{booking.start_date} - {booking.end_date}"
                }
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при создании бронирования: {str(e)}"
            )

    @staticmethod
    def delete_booking(username: str):
        user = UserServices.get_user(username)
        
        booking = BookingRepository.get_booking_by_user(
            user_id=user.id
        )
        
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Бронирование не найдено или не принадлежит пользователю'
            )
        
        if booking.start_date < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Нельзя отменить прошедшее бронирование'
            )
        
        try:
            BookingRepository.delete_booking(booking.id)
            return {'message': 'Бронирование успешно отменено'}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при отмене бронирования: {str(e)}"
            )