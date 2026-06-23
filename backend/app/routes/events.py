from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.event import Event

router = APIRouter(prefix="/events", tags=["Events"])


@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()


@router.post("/")
def create_event(
    title: str,
    event_type: str,
    event_date: str,
    user_id: str,
    db: Session = Depends(get_db)
):
    event = Event(
        title=title,
        event_type=event_type,
        event_date=event_date,
        user_id=user_id
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


@router.post("/sync")
def sync_calendar():
    return {"message": "Calendar sync placeholder"}