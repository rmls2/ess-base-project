from fastapi import APIRouter
from src.api import pagamento

api_router = APIRouter()
api_router.include_router(pagamento.router, prefix="/pagamento", tags=["pagamento"])