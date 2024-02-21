from fastapi import APIRouter, status ## Depends
from src.schemas.response import HttpResponseModel
from src.schemas.attraction import AttractionModel
from src.service.impl.attraction_service import AttractionService

router = APIRouter()

@router.get(
    "/{attraction_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an attraction by attraction ID",
    tags=["attractions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got attraction by attraction id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)

def get_attraction(attraction_id: str) -> HttpResponseModel:
    item_get_response = AttractionService.get_attraction(attraction_id)
    return item_get_response


@router.get(
    "/{attraction_id}/get_images",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve all images by attraction ID",
    tags=["attractions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got all images by attraction id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)

def get_images(attraction_id: str) -> HttpResponseModel:
    item_get_response = AttractionService.get_images(attraction_id)
    return item_get_response

@router.get(
    "/{attraction_id}/get_reviews",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve all reviews by attraction ID",
    tags=["attractions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got all reviews by attraction id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)

def get_reviews(attraction_id: str) -> HttpResponseModel:
    item_get_response = AttractionService.get_reviews(attraction_id)
    return item_get_response





