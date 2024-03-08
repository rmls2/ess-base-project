from pydantic import BaseModel

class ReviewModel(BaseModel):
    user: str
    attraction: str
    quality: int
    price: int

class ReviewUpdateModel(BaseModel):
    user: str
    attraction: str
    newQuality: int
    newPrice: int

class ReviewDeleteModel(BaseModel):
    user: str
    attraction: str


