from fastapi import APIRouter

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
def get_weather():
    return {
        "temperature": 34,
        "condition": "Sunny",
        "humidity": 60
    }