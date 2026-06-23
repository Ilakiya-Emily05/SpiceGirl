from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class OutfitCreate(BaseModel):
    occasion: str
    clothing_ids: List[UUID]


class OutfitResponse(BaseModel):
    id: UUID
    user_id: UUID
    occasion: str
    score: int

    # 🔥 AI EXPLANATION LAYER
    explanation: Optional[str] = None
    clothing_ids: List[UUID]

    class Config:
        from_attributes = True