from pydantic import BaseModel

class HotelSchema(BaseModel):
    title: str
    description: str