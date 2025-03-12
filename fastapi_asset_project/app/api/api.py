from fastapi import APIRouter
from app.api.endpoints import assets

api_router = APIRouter()

# Include the assets router with the same prefix as Django
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
