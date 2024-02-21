from typing import Optional
from pydantic import BaseModel

class PromotionModel(BaseModel):
    user: str
    adm: bool
    hotel: str
    room_id: str
    reservationValue: float
    discountValue: float


class PromotionUpdateModel(BaseModel):
    user: str
    adm: bool
    room_id: str
    currentDiscountValue: float
    newDiscountValue: float

class PromotionDeleteModel(BaseModel):
    user: str
    adm: bool
    room_id: str