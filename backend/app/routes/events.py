from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.get("/")
def get_events():
    return []


@router.post("/sync")
def sync_calendar():
    return {
        "message": "Calendar synced"
    }