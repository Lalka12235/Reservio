from sqlalchemy import select,insert,update,delete

from app.config.session import Session
from app.schemas.room_category_schema import RoomCategorySchema

from app.models.room_category_model import RoomCategoryModel

from app.services.hotel_service import HotelService


class RoomCategoryRepository:

    @staticmethod
    def get_all_room_category_by_hotel(hotel_id: int):
        with Session() as session:

            stmt = select(RoomCategoryModel).where(RoomCategoryModel.hotel_id == hotel_id)
            result = session.execute(stmt).fetchall()
            return result
        
    
    @staticmethod
    def get_room_category_by_title(hotel_id,title_category):
        with Session() as session:
            stmt = select(RoomCategoryModel).where(
                RoomCategoryModel.hotel_id == hotel_id, 
                RoomCategoryModel.title == title_category,
                )
            
            result = session.execute(stmt)
            return result
        
    
    @staticmethod
    def create_room_category(hotel_id: int,category: RoomCategorySchema):
        with Session() as session:
            new_room_category = RoomCategoryModel(
                title_category=category.title,
                description=category.description,
                hotel_id=hotel_id,
            )

            session.add(new_room_category)
            session.commit()
            
            return new_room_category
        
    @staticmethod
    def update_room_category(category: RoomCategorySchema):
        with Session() as session:
            upd_room_category = RoomCategoryModel(
                title_category=category.title,
                description=category.description,
            )

            session.add(upd_room_category)
            session.commit()

            return upd_room_category
        
    
    @staticmethod
    def delete_room_category(hotel_id: int,title_category):
        with Session() as session:

            stmt = delete(RoomCategoryModel).where(RoomCategoryModel.hotel_id == hotel_id, RoomCategoryModel.title == title_category)
            session.execute(stmt)
            return hotel_id,title_category
        
    