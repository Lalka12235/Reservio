from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings

engine = create_engine(
    url=settings.sync_db_url,
    echo=False, #для отладки включить
)

Session = sessionmaker(bind=engine)