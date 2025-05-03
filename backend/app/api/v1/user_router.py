from fastapi import APIRouter

from app.services.user_service import UserServices
from app.schemas.user_schema import UserRegisterSchema, UserLoginSchema

user = APIRouter(
    tags=['User']
)



@user.get('/api/v1/{username}')
async def get_user(username: str):
    return UserServices.get_user(username)


@user.post('/api/v1/register')
async def register_user(user: UserRegisterSchema):
    return UserServices.register_user(user)


@user.delete('/api/v1/{username}')
async def delete_user(user: UserLoginSchema):
    return UserServices.delete_user(user)