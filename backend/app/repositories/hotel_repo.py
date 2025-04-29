from sqlalchemy import select,insert,delete,update
from app.config.session import Session
from app.models.temp_models import HotelModel

from app.schemas.hotel_schema import HotelSchema


class HotelReposotory:

    @staticmethod
    def get_hotel_by_title(title):
        with Session() as session:
            stmt = select(HotelModel).where(HotelModel.title == title)
            return session.execute(stmt).scalar_one_or_none()
        

    @staticmethod
    def create_info_about_hotel(hotel: HotelSchema):
        with Session() as session:
            new_hotel = HotelModel(
                title=hotel.title,
                description=hotel.description,
            )

            session.add(new_hotel)
            session.commit()

            return
        
    
    @staticmethod
    def update_info_about_hotel(old_title,hotel: HotelSchema):
        with Session() as session:
            stmt = update(HotelModel).where(HotelModel.title == old_title).values(title=hotel.title,description=hotel.description)
            session.execute(stmt)
            session.commit()
            return
        
    @staticmethod
    def delete_hotel(title):
        with Session() as session:
            stmt = delete(HotelModel).where(HotelModel.title == title)
            session.execute(stmt)
            session.commit()
            return