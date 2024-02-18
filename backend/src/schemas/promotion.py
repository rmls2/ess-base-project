from typing import Optional
from pydantic import BaseModel

class PromotionModel(BaseModel):
    user: str
    adm: bool
    hotel: str
    reservationValue: float
    discountValue: float


class PromotionUpdateModel(BaseModel):
    user: str
    adm: bool
    hotel: str
    currentDiscountValue: float
    newDiscountValue: float

class PromotionDeleteModel(BaseModel):
    user: str
    adm: bool
    hotel: str