from fastapi import APIRouter

from app.services.user_service import UserServices
from app.schemas.user_schema import UserRegisterSchema, UserLoginSchema

user = APIRouter(
    prefix="/api/v1/users",
    tags=['User']
)



@user.get('/{username}')
async def get_user(username: str):
    return UserServices.get_user(username)


@user.post('/register')
async def register_user(user: UserRegisterSchema):
    return UserServices.register_user(user)


@user.delete('/{username}')
async def delete_user(user: UserLoginSchema):
    return UserServices.delete_user(user)