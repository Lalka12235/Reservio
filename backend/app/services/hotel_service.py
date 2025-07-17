from fastapi import HTTPException, status
from app.repositories.hotel_repo import HotelRepository
from app.schemas.hotel_schema import HotelSchema
from sqlalchemy.orm import Session

class HotelService:

    @staticmethod
    def get_hotel_by_title(db: Session,title: str):
        hotel = HotelRepository.get_hotel_by_title(db,title)
        if not hotel:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Hotel not found'
            ) 
        return hotel.id

    @staticmethod
    def create_info_about_hotel(db: Session,hotel_data: HotelSchema):
        existing = HotelRepository.get_hotel_by_title(db,hotel_data.title)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Hotel already exists'
            )
        result = HotelRepository.create_info_about_hotel(db,hotel_data)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not created'
            )
        return {'message': 'Hotel created successfully','title': hotel_data.title,'description': hotel_data.description}

    @staticmethod
    def update_info_about_hotel(db: Session,old_title: str, hotel_data: HotelSchema):
        existing = HotelRepository.get_hotel_by_title(db,old_title)
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Hotel not found'
            )
        result = HotelRepository.update_info_about_hotel(db,old_title, hotel_data)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not updated'
            )
        return {'message': 'Hotel updated successfully','title': hotel_data.title,'dedscription': hotel_data.description}

    @staticmethod
    def delete_hotel(db: Session,title: str):
        hotel = HotelRepository.get_hotel_by_title(db,title)
        if not hotel:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Hotel not found'
            )
        result = HotelRepository.delete_hotel(db,title)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not deleted'
            )
        return {'message': 'Hotel deleted successfully','title': title}
