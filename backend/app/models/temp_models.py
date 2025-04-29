from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    username: Mapped[str]
    password_hash: Mapped[str]

    bookings: Mapped[list['BookingModel']] = relationship(back_populates='user')


class HotelModel(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    rating: Mapped[float]

    room_categories: Mapped[list['RoomCategoryModel']] = relationship(back_populates='hotel')
    rooms: Mapped[list['RoomModel']] = relationship(back_populates='hotel')
    bookings: Mapped[list['BookingModel']] = relationship(back_populates='hotel')


class RoomCategoryModel(Base):
    __tablename__ = 'room_categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))

    hotel: Mapped['HotelModel'] = relationship(back_populates='room_categories')
    rooms: Mapped[list['RoomModel']] = relationship(back_populates='category')


class RoomModel(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]  # номер комнаты
    title: Mapped[str]   # название (например, "Deluxe Suite")
    description: Mapped[str]
    price: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey('room_categories.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))

    hotel: Mapped['HotelModel'] = relationship(back_populates='rooms')
    category: Mapped['RoomCategoryModel'] = relationship(back_populates='rooms')
    bookings: Mapped[list['BookingModel']] = relationship(back_populates='room')


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
