from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    # 🔥 AI PROFILE LAYER (future personalization hook)
    favorite_color: Optional[str] = None
    favorite_style: Optional[str] = None

    class Config:
        from_attributes = True