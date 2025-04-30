from pydantic import BaseModel
from datetime import datetime

class BookingSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    