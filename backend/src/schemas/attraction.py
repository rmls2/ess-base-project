from pydantic import BaseModel
from src.schemas import reviews

class AttractionModel(BaseModel):
    attraction_id: str
    name: str
    images: list[str] 
    generalInfo: list[str]
    price: float
    reviews: list[reviews.ReviewModel]
    relatedAttractions: list[str]




