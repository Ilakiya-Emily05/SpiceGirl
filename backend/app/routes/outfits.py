from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.outfit import Outfit

router = APIRouter(prefix="/outfits", tags=["Outfits"])


@router.get("/")
def get_outfits(db: Session = Depends(get_db)):
    return db.query(Outfit).all()


@router.post("/save")
def save_outfit(
    user_id: str,
    occasion: str,
    score: int,
    explanation: str,
    db: Session = Depends(get_db)
):
    outfit = Outfit(
        user_id=user_id,
        occasion=occasion,
        score=score,
        explanation=explanation
    )

    db.add(outfit)
    db.commit()
    db.refresh(outfit)

    return outfit