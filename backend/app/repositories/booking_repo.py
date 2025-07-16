from sqlalchemy import select,delete,and_,func
from app.schemas.booking_schema import BookingSchema
from app.models.booking_model import BookingModel
from sqlalchemy.orm import Session


class BookingRepository:

    @staticmethod
    def get_conflicting_bookings(db: Session,room_id: int, booking: BookingSchema):
        stmt = select(BookingModel).where(
            and_(
                BookingModel.room_id == room_id,
                BookingModel.start_date < booking.end_date,
                BookingModel.end_date > booking.start_date
            )
        )
        return db.execute(stmt).scalars().all()

    @staticmethod
    def get_count_bookings_by_user(db: Session,user_id: int) -> int:
        stmt = select(func.count()).select_from(BookingModel).where(
            BookingModel.user_id == user_id
        )
        return db.execute(stmt).scalar()

    @staticmethod
    def get_booking_by_user(db: Session,user_id: int,):
        stmt = select(BookingModel).where(BookingModel.user_id == user_id)
        result = db.execute(stmt).scalar_one_or_none()
        return result
        
    @staticmethod
    def get_all_booking_by_user(db: Session,user_id: int):
        stmt = select(BookingModel).where(BookingModel.user_id == user_id)
        result = db.execute(stmt).fetchall()
        return result
        
    
    @staticmethod
    def create_booking(db: Session,booking: BookingSchema, hotel_id: int, room_id: int,user_id):
        new_booking = BookingModel(
            start_date=booking.start_date,
            end_date=booking.end_date,
            hotel_id=hotel_id,
            room_id=room_id,
            user_id=user_id
        )

        db.add(new_booking)
        db.commit()

        return new_booking
        
    
    @staticmethod
    def delete_booking(db: Session,user_id: int):
        stmt = delete(BookingModel).where(BookingModel.user_id == user_id)
        result = db.execute(stmt)
        return result