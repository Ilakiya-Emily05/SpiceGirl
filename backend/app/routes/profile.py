from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.preference import Preference
from app.models.user import User

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("/{user_id}")
def get_profile(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    pref = db.query(Preference).filter(Preference.user_id == user_id).first()

    return {
        "name": user.name if user else None,
        "favorite_color": pref.favorite_color if pref else None,
        "favorite_style": pref.favorite_style if pref else None
    }