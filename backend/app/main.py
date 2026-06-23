from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    auth,
    clothes,
    recommendations,
    weather,
    events,
    outfits,
    profile
)

app = FastAPI(
    title="Spice Girl API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(clothes.router, prefix="/clothes", tags=["Clothes"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(outfits.router, prefix="/outfits", tags=["Outfits"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])


@app.get("/")
def root():
    return {
        "message": "Welcome to Spice Girl"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}