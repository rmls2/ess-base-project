from fastapi import APIRouter
from src.api import items, attractionItems, reviewItems

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(attractionItems.router, prefix="/attractions", tags=["attractions"])
api_router.include_router(reviewItems.router, prefix="/reviews", tags=["reviews"])