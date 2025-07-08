from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.room_model import RoomModel
    from app.models.hotel_model import HotelModel

class RoomCategoryModel(Base):
    __tablename__ = 'room_categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))

    hotel: Mapped['HotelModel'] = relationship(back_populates='room_categories')
    rooms: Mapped[list['RoomModel']] = relationship(back_populates='category')