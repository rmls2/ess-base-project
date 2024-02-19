from pydantic import BaseModel

class ReviewModel(BaseModel):
    user: str
    attraction: str
    quality: int
    price: int

class ReviewUpdateModel(BaseModel):
    user: str
    attraction: str
    currentQuality: int
    currentPrice: int
    newQuality: int
    newPrice: int

class ReviewDeleteModel(BaseModel):
    user: str
    attraction: str


