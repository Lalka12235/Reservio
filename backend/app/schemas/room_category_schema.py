from pydantic import BaseModel

class RoomCategorySchema(BaseModel):
    title: str
    description: str