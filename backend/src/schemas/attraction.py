from pydantic import BaseModel
from src.schemas import reviews

class AttractionModel(BaseModel):
    user: str
    name: str
    images: list[str] ## como posso representar as imagens ?
    generalInfo: list[str] ## ["Info Geral", "endereço", "Horario", ]
    price: float
    reviews: list[reviews.ReviewModel]
    relatedAttractions: list[str]




