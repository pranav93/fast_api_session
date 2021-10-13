import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import Config

config = Config()

# postgresql://postgres:password@localhost/test_database

engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.close()
