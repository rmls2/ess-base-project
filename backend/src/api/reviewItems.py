from fastapi import APIRouter, status ## Depends
from src.schemas.response import HttpResponseModel
from src.schemas.attraction import AttractionModel
from src.schemas.reviews import ReviewModel, ReviewUpdateModel, ReviewDeleteModel
from src.service.impl.review_service import ReviewService

router = APIRouter()

@router.get(
    "/{review_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an review by review ID",
    tags=["reviews"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got review by review id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Item not found",
        }
    },
)

def get_review(review_id: str) -> HttpResponseModel:
    item_get_response = ReviewService.get_review(review_id)
    return item_get_response

@router.post(
    "/register",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Register a review in a attraction",
    tags=["reviews"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully register a review",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)
def add_review(review_request: ReviewModel) -> HttpResponseModel:
    item_get_response = ReviewService.add_review(review_request)
    return item_get_response

@router.put(
    "/update",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Update a review in a attraction",
    tags=["reviews"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully updated review",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)

def update_review(review_request: ReviewUpdateModel) -> HttpResponseModel:
    item_get_response = ReviewService.update_review(review_request)
    return item_get_response

@router.delete(
    "/delete",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Delete a review in a attraction",
    tags=["reviews"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully deleted review",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)
def delete_Review(review_request: ReviewDeleteModel) -> HttpResponseModel:
    item_get_response = ReviewService.delete_review(review_request)
    return item_get_response
