from abc import ABC, abstractmethod

from src.schemas.promotion import PromotionModel, PromotionUpdateModel

class PromotionServiceMeta(ABC):
    @abstractmethod
    def get_promotion(hotel_id: str):
        """Get promotion by hotel id method implementation"""
        pass
    
    @abstractmethod
    def get_current_discount_value(room_id: str):
        """Get current discount value by room id method implementation"""

    @abstractmethod
    def add_promotion(promotion_request: PromotionModel):
        """Add promotion in hotel method implementation"""

    @abstractmethod
    def update_promotion(promotion_request: PromotionUpdateModel):
        """Update promotion in hotel method implementation"""
        pass

    @abstractmethod
    def delete_promotion(key: str, room_id: str):
        """Delete a promotion in hotel method implementation"""
        pass