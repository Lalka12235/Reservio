import logging
from sqlalchemy import select,delete, update
from app.config.session import Session
from app.models.hotel_model import HotelModel
from app.schemas.hotel_schema import HotelSchema

logger = logging.getLogger(__name__)

class HotelRepository:

    @staticmethod
    def get_hotel_by_title(title: str):
        with Session() as session:
            stmt = select(HotelModel).where(HotelModel.title == title)
            result = session.execute(stmt).scalar_one_or_none()
            logger.info(f"Получен отель с названием: {title}")
            return result

    @staticmethod
    def create_info_about_hotel(hotel: HotelSchema):
        with Session() as session:
            new_hotel = HotelModel(
                title=hotel.title,
                description=hotel.description,
            )
            session.add(new_hotel)
            session.commit()
            logger.info(f"Создан отель: {hotel.title}")
            return new_hotel.id

    @staticmethod
    def update_info_about_hotel(old_title: str, hotel: HotelSchema):
        with Session() as session:
            stmt = (
                update(HotelModel)
                .where(HotelModel.title == old_title)
                .values(title=hotel.title, description=hotel.description)
            )
            result = session.execute(stmt)
            session.commit()
            logger.info(f"Обновлён отель: {old_title} -> {hotel.title}")
            return result

    @staticmethod
    def delete_hotel(title: str):
        with Session() as session:
            stmt = delete(HotelModel).where(HotelModel.title == title)
            result = session.execute(stmt)
            session.commit()
            logger.info(f"Удалён отель с названием: {title}")
            return result
