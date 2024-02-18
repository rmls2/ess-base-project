from fastapi import APIRouter
from backend.src.api import promotion_items
from src.api import items

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(promotion_items.router, prefix="/promotions", tags=["promotions"])