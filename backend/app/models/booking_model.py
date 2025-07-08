from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user_model import UserModel
    from app.models.room_model import RoomModel
    from app.models.hotel_model import HotelModel


class BookingModel(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['UserModel'] = relationship(back_populates='bookings')
    room: Mapped['RoomModel'] = relationship(back_populates='bookings')
    hotel: Mapped['HotelModel'] = relationship(back_populates='bookings')