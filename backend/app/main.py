from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.booking_router import booking
from app.api.v1.hotel_router import hotel
from app.api.v1.room_category_router import room_category
from app.api.v1.room_router import room
from app.api.v1.user_router import user

from app.logger.log_config import configure_logging
from app.middleware.logging_middleware import LogMiddleware

configure_logging()




app = FastAPI()

app.add_middleware(LogMiddleware)

@app.get('/ping')
async def ping():
    return 'Server is work'

origins = [
    "http://localhost",  
    "http://localhost:8080",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(booking)
app.include_router(hotel)
app.include_router(room_category)
app.include_router(room)
app.include_router(user)