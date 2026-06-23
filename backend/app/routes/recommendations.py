from fastapi import APIRouter

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.post("/")
def generate_recommendation():
    return {
        "recommendations": []
    }