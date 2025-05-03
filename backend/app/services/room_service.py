from fastapi import HTTPException,status
from app.repositories.room_repo import RoomRepository
from app.schemas.room_schema import RoomSchema

from app.services.hotel_service import HotelService
from app.services.room_category_service import RoomCategoryService

class RoomService:

    @staticmethod
    def get_room_by_title(title_hotel: str,title_room: str):
        hotel = HotelService.get_hotel_by_title(title_hotel)

        room = RoomRepository.get_room_by_title(hotel.id,title_room)

        if not room:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Room not found'
            )
        
        return room
    
    @staticmethod
    def get_all_room_by_hotel(title_hotel: str):
        hotel = HotelService.get_hotel_by_title(title_hotel)

        rooms = RoomRepository.get_all_room_by_hotel(hotel.id)

        if not rooms:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Room not found'
            )
        
        return {'message': 'success','rooms':{[room for room in rooms]}}
    
    @staticmethod
    def create_room(room: RoomSchema,title_hotel: str, title_category: str):
        hotel = HotelService.get_hotel_by_title(title_hotel)

        category = RoomCategoryService.get_room_category_by_title(hotel.id,title_category)

        result = RoomRepository.create_room(room,hotel.id,category.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                deatil='Not created'
            )
        
        return {'message': 'success','create': result}
    
    @staticmethod
    def update_room(old_title: str, room: RoomSchema, title_category: str):
        hotel = HotelService.get_hotel_by_title(old_title)

        category = RoomCategoryService.get_room_category_by_title(hotel.id,title_category)

        result = RoomRepository.update_room(old_title,room,category.id,hotel.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not update'
            )
        
        return {'message': 'success','update': result}
    

    @staticmethod
    def delete_room(title_room: str, title_hotel: str):
        hotel = HotelService.get_hotel_by_title(title_hotel)

        result = RoomRepository.delete_room(title_room,hotel.id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not delete'
            )
        
        return {'message': 'success','delete': result}
