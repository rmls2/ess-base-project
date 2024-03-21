from src.schemas.response import HttpResponseModel, HTTPResponses
from src.service.meta.attraction_service_meta import AttractionServiceMeta
from src.db.__init__ import database as db
from src.schemas.attraction import AttractionModel


class AttractionService(AttractionServiceMeta):
    @staticmethod
    def get_attraction(attraction_id: str) -> HttpResponseModel:
        """ Get attraction by attraction id method implementation"""
        item = db.get_item_by_attraction_id("attraction", attraction_id)
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        else:
            return HttpResponseModel(
                    message=HTTPResponses.ITEM_FOUND().message,
                    status_code=HTTPResponses.ITEM_FOUND().status_code,
                    data=item,
                )
    
    @staticmethod
    def get_images(attraction_id: str) -> HttpResponseModel:
        """ Get all images by attraction id method implementation"""
        attraction = db.get_item_by_attraction_id("attraction", attraction_id)
        item = attraction["images"]
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        else:
            return HttpResponseModel(
                    message=HTTPResponses.ITEM_FOUND().message,
                    status_code=HTTPResponses.ITEM_FOUND().status_code,
                    data=item,
                )

    @staticmethod
    def get_reviews(attraction_id: str) -> HttpResponseModel:
        """ Get all reviews by attraction id method implementation"""
        attraction = db.get_item_by_attraction_id("attraction", attraction_id)
        item = attraction["reviews"]
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        else:
            return HttpResponseModel(
                    message=HTTPResponses.ITEM_FOUND().message,
                    status_code=HTTPResponses.ITEM_FOUND().status_code,
                    data=item,
                )

    @staticmethod
    def add_attraction(attractionrequest: AttractionModel) -> HttpResponseModel:
        """ Create a attraction method implementation"""
        item = db.insert_item("attraction", attractionrequest.model_dump())
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_CREATED().message,
                status_code=HTTPResponses.ITEM_CREATED().status_code
            )
        item["_id"] = str(item["_id"])
        return HttpResponseModel(
            message=HTTPResponses.ITEM_CREATED().message,
            status_code=HTTPResponses.ITEM_CREATED().status_code
        )


