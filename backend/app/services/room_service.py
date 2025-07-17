from fastapi import HTTPException,status
from app.repositories.room_repo import RoomRepository
from app.schemas.room_schema import RoomSchema

from app.services.hotel_service import HotelService
from app.services.room_category_service import RoomCategoryService
from sqlalchemy.orm import Session

class RoomService:

    @staticmethod
    def get_room_by_title(db: Session,title_hotel: str,title_room: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        room = RoomRepository.get_room_by_title(db,hotel,title_room)

        if not room:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Room not found'
            )
        
        return {'message': 'success','detail': room}
    
    @staticmethod
    def get_all_room_by_hotel(db: Session,title_hotel: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        rooms = RoomRepository.get_all_room_by_hotel(db,hotel)

        if not rooms:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Room not found'
            )
        
        return {'message': 'success','rooms':{[room for room in rooms]}}
    
    @staticmethod
    def create_room(db: Session,room: RoomSchema,title_hotel: str, title_category: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        category = RoomCategoryService.get_room_category_by_title(db,hotel,title_category)

        result = RoomRepository.create_room(db,room,hotel,category.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                deatil='Not created'
            )
        
        return {'message': 'success','create': result}
    
    @staticmethod
    def update_room(db: Session,old_title: str, room: RoomSchema, title_category: str):
        hotel = HotelService.get_hotel_by_title(db,old_title)

        category = RoomCategoryService.get_room_category_by_title(db,hotel,title_category)

        result = RoomRepository.update_room(db,old_title,room,category.id,hotel)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not update'
            )
        
        return {'message': 'success','update': result}
    

    @staticmethod
    def delete_room(db: Session,title_room: str, title_hotel: str):
        hotel = HotelService.get_hotel_by_title(db,title_hotel)

        result = RoomRepository.delete_room(db,title_room,hotel)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not delete'
            )
        
        return {'message': 'success','delete': result}
