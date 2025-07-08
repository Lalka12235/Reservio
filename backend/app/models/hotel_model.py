from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.room_category_model import RoomCategoryModel
    from app.models.booking_model import BookingModel
    from app.models.room_model import RoomModel


class HotelModel(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    rating: Mapped[float]

    room_categories: Mapped[list['RoomCategoryModel']] = relationship(back_populates='hotel')
    rooms: Mapped[list['RoomModel']] = relationship(back_populates='hotel')
    bookings: Mapped[list['BookingModel']] = relationship(back_populates='hotel')
