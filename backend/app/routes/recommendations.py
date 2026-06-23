from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.post("/")
def generate_recommendation(user_id: str, occasion: str, db: Session = Depends(get_db)):
    # 🔥 THIS WILL LATER CALL YOUR AI ENGINE
    return {
        "user_id": user_id,
        "occasion": occasion,
        "recommendations": [
            {
                "outfit": ["White Shirt", "Grey Trousers"],
                "score": 92,
                "reason": "Formal + weather appropriate + user preference match"
            }
        ]
    }