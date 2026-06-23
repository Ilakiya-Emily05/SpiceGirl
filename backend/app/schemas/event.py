from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EventCreate(BaseModel):
    title: str
    event_type: str
    event_date: datetime


class EventResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    event_type: str
    event_date: datetime

    class Config:
        from_attributes = True