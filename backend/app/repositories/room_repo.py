from sqlalchemy import select,update,delete
from sqlalchemy.orm import Session
from app.schemas.room_schema import RoomSchema
from app.models.room_model import RoomModel



class RoomRepository:

    @staticmethod
    def get_room_by_title(db: Session,hotel_id: int,title_room: str):
        stmt = select(RoomModel).where(RoomModel.hotel_id == hotel_id,RoomModel.title == title_room)
        result = db.execute(stmt).scalar_one_or_none()
        return result
        
    @staticmethod
    def get_all_room_by_hotel(db: Session,hotel_id: int):
        stmt = select(RoomModel).where(RoomModel.hotel_id == hotel_id)
        result = db.execute(stmt).fetchall()
        return result
        
    @staticmethod
    def create_room(db: Session,room: RoomSchema,hotel_id: int,category_id: int):
        new_room = RoomModel(
            title=room.title,
            description=room.description,
            price=room.price,
            hotel_id=hotel_id,
            category_id=category_id
        )

        db.add(new_room)
        db.commit()

        return new_room
        
    @staticmethod
    def update_room(db: Session,old_title: str,room: RoomSchema,category_id: int,hotel_id: int):
        stmt = update(RoomModel).where(RoomModel.title == old_title).values(
            title=room.title,
            description=room.description,
            price=room.price,
            category_id=category_id,
        )
        result = db.execute(stmt)
        db.commit()
        return result
        

    @staticmethod
    def delete_room(db: Session,title_room: str,hotel_id: int):
        stmt = delete(RoomModel).where(RoomModel.title == title_room,RoomModel.hotel_id == hotel_id)
        result = db.execute(stmt)
        return result
        
    
