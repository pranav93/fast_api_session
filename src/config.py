from pydantic import BaseSettings


class Config(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str
