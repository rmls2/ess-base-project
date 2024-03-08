from pydantic import BaseModel
from src.schemas import reviews

class AttractionModel(BaseModel):
    user: str
    name: str
    images: list[str] 
    generalInfo: list[str]
    price: float
    reviews: list[reviews.ReviewModel]
    relatedAttractions: list[str]




