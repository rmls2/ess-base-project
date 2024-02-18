from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.promotion_service_meta import PromotionServiceMeta
from src.db.__init__ import database as db
from src.schemas.promotion import PromotionModel, PromotionUpdateModel, PromotionDeleteModel


class PromotionService(PromotionServiceMeta):
    @staticmethod
    def get_promotion(hotel_id: str) -> HttpResponseModel:
        """Get promotion by hotel id method implementation"""
        item = db.get_item_by_hotel_id('promotions', hotel_id)
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
    def add_promotion(promotion_request: PromotionModel) -> HttpResponseModel:
        """Add promotion in hotel method implementation"""
        if promotion_request.adm:
            if promotion_request.discountValue > 0 and promotion_request.discountValue <= (promotion_request.reservationValue * 0.5) and promotion_request.discountValue != None:
                item = db.insert_promotion('promotions', promotion_request.dict())
                if not item:
                    return HttpResponseModel(
                        message=HTTPResponses.PROMOTION_NOT_CREATED().message,
                        status_code=HTTPResponses.PROMOTION_NOT_CREATED().status_code,
                    )
                item["_id"] = str(item["_id"])
                return HttpResponseModel(
                        message=HTTPResponses.PROMOTION_CREATED().message,
                        status_code=HTTPResponses.PROMOTION_CREATED().status_code,
                        data=item,
                    )
            else:
                return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_CREATED().message,
                    status_code=HTTPResponses.PROMOTION_NOT_CREATED().status_code,
                )   
        else:
            return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_CREATED().message,
                    status_code=HTTPResponses.PROMOTION_NOT_CREATED().status_code,
            )
        
    @staticmethod
    def update_promotion(promotion_request: PromotionUpdateModel) -> HttpResponseModel:
        """Update promotion in hotel method implementation"""
        if promotion_request.adm:
            hotel_discount = db.find_hotel_by_name(promotion_request.hotel)["reservationValue"]
            if not hotel_discount:
                return HttpResponseModel(
                    message=HTTPResponses.ITEM_NOT_FOUND().message,
                    status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
                )
            else:
                if promotion_request.newDiscountValue > 0 and promotion_request.newDiscountValue <= (hotel_discount * 0.5) and promotion_request.newDiscountValue != None:
                    item = db.update_promotion(promotion_request.hotel, promotion_request.newDiscountValue)
                    if not item:
                        return HttpResponseModel(
                            message=HTTPResponses.PROMOTION_NOT_UPDATED().message,
                            status_code=HTTPResponses.PROMOTION_NOT_UPDATED().status_code,
                        )
                    item["_id"] = str(item["_id"])
                    return HttpResponseModel(
                            message=HTTPResponses.PROMOTION_UPDATED().message,
                            status_code=HTTPResponses.PROMOTION_UPDATED().status_code,
                            data=item,
                        )
                else:
                    return HttpResponseModel(
                        message=HTTPResponses.PROMOTION_NOT_UPDATED().message,
                        status_code=HTTPResponses.PROMOTION_NOT_UPDATED().status_code,
                    )  
        else:
            return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_CREATED().message,
                    status_code=HTTPResponses.PROMOTION_NOT_CREATED().status_code,
            )
        
    @staticmethod
    def delete_promotion(promotion_request: PromotionDeleteModel) -> HttpResponseModel:
        """Delete a promotion in hotel method implementation"""
        if promotion_request.adm:
            hotel_discount = db.find_hotel_by_name(promotion_request.hotel)
            if not hotel_discount:
                return HttpResponseModel(
                    message=HTTPResponses.ITEM_NOT_FOUND().message,
                    status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
                )
            else:
                hotel_discount["_id"] = str(hotel_discount["_id"])
                hotel_removed = db.delete_promotion(hotel_discount["hotel"])
                return HttpResponseModel(
                            message=HTTPResponses.PROMOTION_DELETED().message,
                            status_code=HTTPResponses.PROMOTION_DELETED().status_code,
                            data=hotel_removed,
                        )
        else:
            return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_DELETED().message,
                    status_code=HTTPResponses.PROMOTION_NOT_DELETED().status_code,
            )