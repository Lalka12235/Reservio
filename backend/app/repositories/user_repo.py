from sqlalchemy import select,delete,insert

from app.models.user_model import UserModel
from sqlalchemy.orm import Session
from app.utils.hash import make_hash_pass
from app.schemas.user_schema import UserRegisterSchema, UserLoginSchema

class UserRepository:

    @staticmethod
    def get_user(db: Session,username: str):
         stmt = select(UserModel).where(UserModel.username == username)
         user =  db.execute(stmt).scalar_one_or_none()
         return user
        
    @staticmethod
    def register_user(db: Session,user: UserRegisterSchema):
         hash_pass = make_hash_pass(user.password)

         stmt = insert(UserModel).values(email=user.email,username=user.username,hashed_password=hash_pass)
         db.execute(stmt)
         db.commit()
        
    @staticmethod
    def delete_user(db: Session,user: UserLoginSchema):
         hash_pass = make_hash_pass(user.password)

         stmt = delete(UserModel).where(UserModel.username == user.username,UserModel.hashed_password == hash_pass).returning(UserModel.id)
         db.execute(stmt)
         db.commit()