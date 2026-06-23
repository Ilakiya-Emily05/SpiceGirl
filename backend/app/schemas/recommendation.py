from pydantic import BaseModel
from typing import List, Optional


class RecommendationRequest(BaseModel):
    occasion: str
    temperature: float
    weather_condition: str

    # 🔥 AI CONTEXT INPUT
    user_id: str


class RecommendedOutfit(BaseModel):
    top: str
    bottom: str
    shoes: str
    score: float

    # 🔥 WHY AI DID THIS (CRITICAL FOR DEMO / PAPER)
    reasons: List[str]


class RecommendationResponse(BaseModel):
    recommendations: List[RecommendedOutfit]

    # 🔥 META (makes it look intelligent in API responses)
    strategy: Optional[str] = "rule_based_v1"