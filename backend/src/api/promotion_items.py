from fastapi import APIRouter, status
from src.schemas.response import HttpResponseModel
from src.schemas.promotion import PromotionModel, PromotionUpdateModel
from src.service.impl.promotion_service import PromotionService 

router = APIRouter()

@router.get(
    "/{room_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve an promotion by room ID",
    tags=["promotions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got promotion by room id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Promotion not found",
        }
    },
)
def get_promotion(room_id: str) -> HttpResponseModel:
    item_get_response = PromotionService.get_promotion(room_id)
    return item_get_response

@router.get(
    "/{room_id}/current",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Retrieve current discount value by room ID",
    tags=["promotions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully got discount value by room id",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Discount not found",
        }
    },
)
def get_current_discount_value (room_id: str) -> HttpResponseModel:
    item_get_response = PromotionService.get_current_discount_value(room_id)
    return item_get_response

@router.post(
    "/register",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Register a promotion in a hotel",
    tags=["promotions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully register a promotion",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)
def add_promotion(promotion_request: PromotionModel) -> HttpResponseModel:
    item_get_response = PromotionService.add_promotion(promotion_request)
    return item_get_response

@router.put(
    "/update",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Update a promotion in a hotel",
    tags=["promotions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully updated promotion",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)
def update_promotion(promotion_request: PromotionUpdateModel) -> HttpResponseModel:
    item_get_response = PromotionService.update_promotion(promotion_request)
    return item_get_response

@router.delete(
    "/delete/{key}/{room_id}",
    response_model=HttpResponseModel,
    status_code=status.HTTP_200_OK,
    description="Delete a promotion in a hotel",
    tags=["promotions"],
    responses={
        status.HTTP_200_OK: {
            "model": HttpResponseModel,
            "description": "Successfully deleted promotion",
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request",
        }
    },
)
def delete_promotion(key: str, room_id: str) -> HttpResponseModel:
    item_get_response = PromotionService.delete_promotion(key, room_id)
    return item_get_response