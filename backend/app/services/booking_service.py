from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy import and_

from app.repositories.booking_repo import BookingRepository
from app.services.user_service import UserServices
from app.services.room_service import RoomService
from app.services.hotel_service import HotelService
from app.schemas.booking_schema import BookingSchema


class BookingService:

    @staticmethod
    def _check_booking_dates(start_date: datetime, end_date: datetime):
        if start_date >= end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Дата окончания должна быть позже даты начала"
            )
        
        if start_date < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Нельзя бронировать на прошедшую дату"
            )

    @staticmethod
    def _check_room_availability(room_id: int, start_date: datetime, end_date: datetime):
        conflicting_bookings = BookingRepository.get_conflicting_bookings(
            room_id=room_id,
            start_date=start_date,
            end_date=end_date
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
        # Получаем необходимые объекты
        user = UserServices.get_user(username)
        hotel = HotelService.get_hotel_by_title(title_hotel)
        room = RoomService.get_room_by_title(title_hotel, title_room)

        # Проверки перед созданием бронирования
        BookingService._check_booking_dates(booking.start_date, booking.end_date)
        BookingService._check_room_availability(room.id, booking.start_date, booking.end_date)

        # Создаем бронирование
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
    def delete_booking(username: str, booking_id: int):
        user = UserServices.get_user(username)
        
        # Проверяем, что бронирование принадлежит пользователю
        booking = BookingRepository.get_booking_by_id_and_user(
            booking_id=booking_id,
            user_id=user.id
        )
        
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Бронирование не найдено или не принадлежит пользователю'
            )
        
        # Проверяем, что не пытаемся отменить прошедшее бронирование
        if booking.start_date < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Нельзя отменить прошедшее бронирование'
            )
        
        # Удаляем бронирование
        try:
            BookingRepository.delete_booking(booking_id)
            return {'message': 'Бронирование успешно отменено'}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при отмене бронирования: {str(e)}"
            )