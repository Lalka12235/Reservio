from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.room_category_model import RoomCategoryModel
    from app.models.booking_model import BookingModel
    from app.models.hotel_model import HotelModel

class RoomModel(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey('room_categories.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))

    hotel: Mapped['HotelModel'] = relationship(back_populates='rooms')
    category: Mapped['RoomCategoryModel'] = relationship(back_populates='rooms')
    bookings: Mapped[list['BookingModel']] = relationship(back_populates='room')