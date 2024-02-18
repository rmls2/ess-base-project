from fastapi import APIRouter
from src.api import items, promotionItems

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(promotionItems.router, prefix="/promotions", tags=["promotions"])