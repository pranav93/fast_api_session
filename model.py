from sqlalchemy import Integer, String, Float
from sqlalchemy.sql.schema import Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    brand = Column(String)
