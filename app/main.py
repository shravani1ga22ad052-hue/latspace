from fastapi import FastAPI

from app.routers.parse import router as parse_router

app = FastAPI(title="LatSpace Intelligent Excel Parser", version="0.2.0")
app.include_router(parse_router)
