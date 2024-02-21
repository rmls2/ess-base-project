from abc import ABC, abstractmethod
from src.schemas.attraction import AttractionModel

class AttractionServiceMeta(ABC):
    @abstractmethod
    def get_attraction(self) -> AttractionModel:
        """Get item by id method definition"""
        pass

    @abstractmethod
    def get_images(self) -> AttractionModel:
        """Get item by id method definition"""
        pass
    

    @abstractmethod
    def get_reviews(self) -> AttractionModel:
        """Get item by id method definition"""
        pass
    

    
