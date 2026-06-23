from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class ClothingCreate(BaseModel):
    name: str
    category: str
    color: str
    season: str
    style: str
    image_url: Optional[str] = None


class ClothingUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    color: Optional[str] = None
    season: Optional[str] = None
    style: Optional[str] = None
    image_url: Optional[str] = None


class ClothingResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    category: str
    color: str
    season: str
    style: str
    image_url: Optional[str]

    class Config:
        from_attributes = True