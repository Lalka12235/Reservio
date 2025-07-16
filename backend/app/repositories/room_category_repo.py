from sqlalchemy import select,delete

from sqlalchemy.orm import Session
from app.schemas.room_category_schema import RoomCategorySchema

from app.models.room_category_model import RoomCategoryModel



class RoomCategoryRepository:

    @staticmethod
    def get_all_room_category_by_hotel(db: Session,hotel_id: int):
        stmt = select(RoomCategoryModel).where(RoomCategoryModel.hotel_id == hotel_id)
        result = db.execute(stmt).fetchall()
        return result
        
    
    @staticmethod
    def get_room_category_by_title(db: Session,hotel_id,title_category):
        stmt = select(RoomCategoryModel).where(
            RoomCategoryModel.hotel_id == hotel_id, 
            RoomCategoryModel.title == title_category,
            )
        
        result = db.execute(stmt)
        return result
        
    
    @staticmethod
    def create_room_category(db: Session,hotel_id: int,category: RoomCategorySchema):
        new_room_category = RoomCategoryModel(
            title_category=category.title,
            description=category.description,
            hotel_id=hotel_id,
        )

        db.add(new_room_category)
        db.commit()
        
        return new_room_category
        
    @staticmethod
    def update_room_category(db: Session,category: RoomCategorySchema):
        upd_room_category = RoomCategoryModel(
            title_category=category.title,
            description=category.description,
        )

        db.add(upd_room_category)
        db.commit()

        return upd_room_category
        
    
    @staticmethod
    def delete_room_category(db: Session,hotel_id: int,title_category):
        stmt = delete(RoomCategoryModel).where(RoomCategoryModel.hotel_id == hotel_id, RoomCategoryModel.title == title_category)
        db.execute(stmt)
        return hotel_id,title_category
        
    