from pydantic import BaseModel, EmailStr


class UserRegisterSchema(BaseModel):
    email:EmailStr
    username: str
    password: str

class UserLoginSchema(BaseModel):
    username: str
    password: str