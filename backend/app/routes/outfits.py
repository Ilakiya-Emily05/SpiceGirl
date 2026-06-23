from fastapi import APIRouter

router = APIRouter(
    prefix="/outfits",
    tags=["Outfits"]
)


@router.get("/")
def get_outfits():
    return []


@router.post("/save")
def save_outfit():
    return {
        "message": "Outfit saved"
    }