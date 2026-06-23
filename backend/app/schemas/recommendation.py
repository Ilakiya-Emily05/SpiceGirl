from pydantic import BaseModel
from typing import List


class RecommendationRequest(BaseModel):
    occasion: str
    temperature: float
    weather_condition: str


class RecommendedOutfit(BaseModel):
    top: str
    bottom: str
    shoes: str
    score: int
    reasons: List[str]


class RecommendationResponse(BaseModel):
    recommendations: List[RecommendedOutfit]