from fastapi import HTTPException, status
from app.repositories.room_category_repo import RoomCategoryRepository
from app.services.hotel_service import HotelService
from app.schemas.room_category_schema import RoomCategorySchema
from sqlalchemy.orm import Session


class RoomCategoryService:

    @staticmethod
    def get_all_room_category_by_hotel(db: Session,title_hotel: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomCategoryRepository.get_all_room_category_by_hotel(db,hotel.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Category not found'
            )
    
        return {'message': 'success','result': [category for category in result]}
    
    @staticmethod
    def get_room_category_by_title(db: Session,title_hotel: str,title_category: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomCategoryRepository.get_room_category_by_title(db,hotel.id,title_category)

        if not result: 
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Category not found'
            )
        
        return {'message': 'success','result': result}
    

    @staticmethod
    def create_room_category(db: Session,title_hotel: str, category: RoomCategorySchema):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomCategoryRepository.create_room_category(db,hotel.id,category)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not created'
            )
        
        return {'message': 'success','result': result}
    

    @staticmethod
    def update_room_category(db: Session,title_hotel: str, category: RoomCategorySchema):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomCategoryRepository.update_room_category(db,hotel.id,category)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not updated'
            )
        
        return {'message': 'success','result': result}
    

    @staticmethod
    def delete_room_category(db: Session,title_hotel: str, title_category: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomCategoryRepository.delete_room_category(db,hotel.id,title_category)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not deleted'
            )
        
        return {'message': 'success','result': result}

