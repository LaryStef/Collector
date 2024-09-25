from sqlalchemy import Engine, create_engine

from src.config import DB_URL


engine: Engine = create_engine(url=DB_URL)
