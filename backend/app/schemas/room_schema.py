from pydantic import BaseModel

class RoomSchema(BaseModel):
    title: str
    description: str
    price: int
    