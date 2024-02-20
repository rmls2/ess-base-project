from fastapi import APIRouter, status ## Depends
from src.schemas.response import HttpResponseModel
from src.schemas.attraction import AttractionModel
from src.service.impl.attraction_service import AttractionService

router = APIRouter()

@router.get(
    "/{attraction_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an attraction by hotel ID",
    tags=["attractions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got promotion by hotel id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)

def get_attraction(attraction_id: str) -> HttpResponseModel:
    item_get_response = AttractionService.get_attraction(attraction_id)
    return item_get_response




