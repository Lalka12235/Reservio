from sqlalchemy import select,update,delete
from app.config.session import Session
from app.schemas.room_schema import RoomSchema
from app.models.room_model import RoomModel



class RoomRepository:

    @staticmethod
    def get_room_by_title(hotel_id: int,title_room: str):
        with Session() as session:
            stmt = select(RoomModel).where(RoomModel.hotel_id == hotel_id,RoomModel.title == title_room)
            result = session.execute(stmt).scalar_one_or_none()
            return result
        
    @staticmethod
    def get_all_room_by_hotel(hotel_id: int):
        with Session() as session:
            stmt = select(RoomModel).where(RoomModel.hotel_id == hotel_id)
            result = session.execute(stmt).fetchall()
            return result
        
    @staticmethod
    def create_room(room: RoomSchema,hotel_id: int,category_id: int):
        with Session() as session:
            new_room = RoomModel(
                title=room.title,
                description=room.description,
                price=room.price,
                hotel_id=hotel_id,
                category_id=category_id
            )

            session.add(new_room)
            session.commit()

            return new_room
        
    @staticmethod
    def update_room(old_title: str,room: RoomSchema,category_id: int,hotel_id: int):
        with Session() as session:
            stmt = update(RoomModel).where(RoomModel.title == old_title).values(
                title=room.title,
                description=room.description,
                price=room.price,
                category_id=category_id,
            )
            result = session.execute(stmt)
            session.commit()
            return result
        

    @staticmethod
    def delete_room(title_room: str,hotel_id: int):
        with Session() as session:
            stmt = delete(RoomModel).where(RoomModel.title == title_room,RoomModel.hotel_id == hotel_id)
            result = session.execute(stmt)
            return result
        
    
