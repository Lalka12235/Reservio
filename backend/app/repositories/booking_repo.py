from sqlalchemy import select,delete,and_,func
from app.schemas.booking_schema import BookingSchema
from app.models.temp_models import BookingModel
from app.config.session import Session


class BookingRepository:

    @staticmethod
    def get_conflicting_bookings(room_id: int, booking: BookingSchema):
        with Session() as session:
            stmt = select(BookingModel).where(
                and_(
                    BookingModel.room_id == room_id,
                    BookingModel.start_date < booking.end_date,
                    BookingModel.end_date > booking.start_date
                )
            )
            return session.execute(stmt).scalars().all()

    @staticmethod
    def get_booking_by_id_and_user(booking_id: int, user_id: int):
        with Session() as session:
            stmt = select(BookingModel).where(
                and_(
                    BookingModel.id == booking_id,
                    BookingModel.user_id == user_id
                )
            )
            return session.execute(stmt).scalar_one_or_none()

    @staticmethod
    def get_count_bookings_by_user(user_id: int) -> int:
        with Session() as session:
            stmt = select(func.count()).select_from(BookingModel).where(
                BookingModel.user_id == user_id
            )
            return session.execute(stmt).scalar()

    @staticmethod
    def get_booking_by_user(user_id: int,):
        with Session() as session:
            stmt = select(BookingModel).where(BookingModel.user_id == user_id)
            result = session.execute(stmt).scalar_one_or_none()
            return result
        
    @staticmethod
    def get_all_booking_by_user(user_id: int):
        with Session() as session:
            stmt = select(BookingModel).where(BookingModel.user_id == user_id)
            result = session.execute(stmt).fetchall()
            return result
        
    
    @staticmethod
    def create_booking(booking: BookingSchema, hotel_id: int, room_id: int,user_id):
        with Session() as session:
            new_booking = BookingModel(
                start_date=booking.start_date,
                end_date=booking.end_date,
                hotel_id=hotel_id,
                room_id=room_id,
                user_id=user_id
            )

            session.add(new_booking)
            session.commit()

            return new_booking
        
    
    @staticmethod
    def delete_booking(user_id: int):
        with Session() as session:
            stmt = delete(BookingModel).where(BookingModel.user_id == user_id)
            result = session.execute(stmt)
            return result