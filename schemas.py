from pydantic import BaseModel
from typing import Optional


class CreateItemRequest(BaseModel):
    name: str
    price: float
    brand: Optional[str]


class UpdateItemRequest(BaseModel):
    name: Optional[str]
    price: Optional[float]
    brand: Optional[str]


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    brand: Optional[str]
