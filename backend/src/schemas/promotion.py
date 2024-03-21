from typing import Optional
from pydantic import BaseModel

class PromotionModel(BaseModel):
    user: str
    adm_key: str
    hotel: str
    room_id: str
    reservationValue: float
    discountValue: float


class PromotionUpdateModel(BaseModel):
    user: str
    adm_key: str
    room_id: str
    currentDiscountValue: float
    newDiscountValue: float