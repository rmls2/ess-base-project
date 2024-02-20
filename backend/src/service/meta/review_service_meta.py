from abc import ABC, abstractmethod
from src.schemas.reviews import ReviewModel, ReviewUpdateModel, ReviewDeleteModel


class ReviewServiceMeta(ABC):
    @abstractmethod
    def get_review(attraction_id: str):
        """Get review by attraction id method implementation"""
        pass

    @abstractmethod
    def add_review(review_request: ReviewModel):
        """Add review in attraction method implementation"""

    @abstractmethod
    def update_review(review_request: ReviewUpdateModel):
        """Update review in attraction method implementation"""
        pass

    @abstractmethod
    def delete_review(review_request: ReviewDeleteModel):
        """Delete a review in attraction method implementation"""
        pass