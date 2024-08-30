from sqlalchemy import create_engine, Engine

from ..config import DB_URL


engine: Engine = create_engine(url=DB_URL)
