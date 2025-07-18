from fastapi import APIRouter,Depends
from app.config.session import get_db
from typing import Annotated
from sqlalchemy.orm import Session


from app.services.user_service import UserServices
from app.schemas.user_schema import UserRegisterSchema, UserLoginSchema

user = APIRouter(
    prefix="/api/v1/users",
    tags=['User']
)

db_dependency = Annotated[Session,Depends(get_db)]

@user.get('/{username}')
async def get_user(db:db_dependency,username: str):
    return UserServices.get_user(db,username)


@user.post('/register')
async def register_user(db:db_dependency,user: UserRegisterSchema):
    return UserServices.register_user(db,user)


@user.delete('/{username}')
async def delete_user(db:db_dependency,user: UserLoginSchema, username: str):
    return UserServices.delete_user(db,user)