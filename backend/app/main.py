from fastapi import FastAPI

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

app.include_router(auth.router)
app.include_router(clothes.router)
app.include_router(recommendations.router)
app.include_router(weather.router)
app.include_router(events.router)
app.include_router(outfits.router)
app.include_router(profile.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Spice Girl"
    }