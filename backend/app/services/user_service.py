from fastapi import HTTPException,status
from app.repositories.user_repo import UserRepository

from app.schemas.user_schema import UserLoginSchema, UserRegisterSchema
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class UserServices:

    @staticmethod
    def get_user(db: Session,username: str):
        logger.debug(f'Попытка получить пользователя: {username}')
        user =  UserRepository.get_user(db,username)
        if user is None:
            logger.error(f'Пользователь не найден: {username}')
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found'
            )
        logger.info(f'Пользователь найден: {username}')
        return {'message': 'User found', 'detail': username}

    @staticmethod
    def register_user(db: Session,user: UserRegisterSchema):
        logger.debug(f'Попытка регистрации пользователя: {user.username}')
        existing_user =  UserRepository.get_user(db,user.username)
        if existing_user:
            logger.error(f'Пользователь уже существует: {user.username}')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )
        user_id =  UserRepository.register_user(db,user)
        logger.info(f'Пользователь успешно зарегистрирован: {user.username}')
        return {'message': 'Account created', 'user_id': user_id}

    @staticmethod
    def delete_user(db: Session,user: UserLoginSchema):
        logger.debug(f'Попытка удаления пользователя: {user.username}')
        deleted_user =  UserRepository.delete_user(db,user)
        if not deleted_user:
            logger.error(f'Не удалось удалить пользователя: {user.username}')
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='User not found or incorrect password'
            )
        logger.info(f'Пользователь удалён: {user.username}')
        return {'message': 'Account deleted', 'user_id': deleted_user}
