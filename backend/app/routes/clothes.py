from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.clothing import Clothing

router = APIRouter(prefix="/clothes", tags=["Clothes"])


@router.get("/")
def get_clothes(db: Session = Depends(get_db)):
    return db.query(Clothing).all()


@router.post("/")
def add_clothing(
    name: str,
    category: str,
    color: str,
    season: str,
    style: str,
    user_id: str,
    db: Session = Depends(get_db)
):
    clothing = Clothing(
        name=name,
        category=category,
        color=color,
        season=season,
        style=style,
        user_id=user_id
    )

    db.add(clothing)
    db.commit()
    db.refresh(clothing)

    return clothing


@router.get("/{clothing_id}")
def get_clothing(clothing_id: str, db: Session = Depends(get_db)):
    item = db.query(Clothing).filter(Clothing.id == clothing_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item


@router.delete("/{clothing_id}")
def delete_clothing(clothing_id: str, db: Session = Depends(get_db)):
    item = db.query(Clothing).filter(Clothing.id == clothing_id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(item)
    db.commit()

    return {"message": "Deleted"}