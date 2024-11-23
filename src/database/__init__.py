from sqlalchemy import Engine, create_engine

from src.config import settings


engine: Engine = create_engine(url=settings.DB_URL)
