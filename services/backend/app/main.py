from fastapi import FastAPI

from app.api.routes import api_router

app = FastAPI(title="CLOAK Backend", version="0.1.0")

@app.get("/health", tags=["health"])  # liveness probe
async def health() -> dict:
    return {"status": "ok"}

app.include_router(api_router, prefix="/api")