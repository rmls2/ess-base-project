from abc import ABC, abstractmethod

from src.schemas.promotion import PromotionModel

class PromotionServiceMeta(ABC):
    @abstractmethod
    def add_promotion(self, hotel_id: str) -> PromotionModel:
        """Get item by id method definition"""
        pass