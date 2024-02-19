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

