from fastapi import HTTPException, status
from app.repositories.room_category_repo import RoomCategoryRepository
from app.services.hotel_service import HotelService
from app.schemas.room_category_schema import RoomCategorySchema


class RoomCategoryService:

    @staticmethod
    def get_all_room_category_by_hotel(title_hotel: str):
        hotel = HotelService.get_hotel_by_title(title_hotel)

        result = RoomCategoryRepository.get_all_room_category_by_hotel(hotel.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Category not found'
            )
    
        return result
    

    @staticmethod