import logging
from sqlalchemy import select,delete, update
from sqlalchemy.orm import Session
from app.models.hotel_model import HotelModel
from app.schemas.hotel_schema import HotelSchema

logger = logging.getLogger(__name__)

class HotelRepository:

    @staticmethod
    def get_hotel_by_title(db: Session,title: str):
        stmt = select(HotelModel).where(HotelModel.title == title)
        result = db.execute(stmt).scalar_one_or_none()
        logger.info(f"Получен отель с названием: {title}")
        return result

    @staticmethod
    def create_info_about_hotel(db: Session,hotel: HotelSchema):
        new_hotel = HotelModel(
            title=hotel.title,
            description=hotel.description,
        )
        db.add(new_hotel)
        db.commit()
        logger.info(f"Создан отель: {hotel.title}")
        return new_hotel.id

    @staticmethod
    def update_info_about_hotel(db: Session,old_title: str, hotel: HotelSchema):
        stmt = (
            update(HotelModel)
            .where(HotelModel.title == old_title)
            .values(title=hotel.title, description=hotel.description)
        )
        result = db.execute(stmt)
        db.commit()
        logger.info(f"Обновлён отель: {old_title} -> {hotel.title}")
        return result

    @staticmethod
    def delete_hotel(db: Session,title: str):
        stmt = delete(HotelModel).where(HotelModel.title == title)
        result = db.execute(stmt)
        db.commit()
        logger.info(f"Удалён отель с названием: {title}")
        return result
