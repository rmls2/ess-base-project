from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.promotion_service_meta import PromotionServiceMeta
from src.db.__init__ import database as db
from src.schemas.promotion import PromotionModel, PromotionUpdateModel


class PromotionService(PromotionServiceMeta):
    @staticmethod
    def get_promotion(room_id: str) -> HttpResponseModel:
        """Get promotion by room id method implementation"""
        item = db.get_value_by_room_id('promotions', room_id)
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.PROMOTION_NOT_FOUND().message,
                status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
            )
        else:
            value = {
                "reservationValue": item["reservationValue"],
                "newValue": item["reservationValue"] - item["discountValue"]
            }
            return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_FOUND().message,
                    status_code=HTTPResponses.PROMOTION_FOUND().status_code,
                    data=value,
                )

    @staticmethod
    def get_current_discount_value(room_id: str) -> HttpResponseModel:
        """Get current discount value by room id method implementation"""
        item = db.get_value_by_room_id('promotions', room_id)
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.PROMOTION_NOT_FOUND().message,
                status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
            )
        else:
            value = {"id": str(item["_id"]), "currentValue": item["discountValue"]}

            return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_FOUND().message,
                    status_code=HTTPResponses.PROMOTION_FOUND().status_code,
                    data=value,
                )
        
    @staticmethod
    def get_room_id(room_name: str, adm_key: str) -> HttpResponseModel:
        if db.check_if_key_is_adm(adm_key):
            room = db.get_room_id_by_room_name(room_name)
            if not room:
                return HttpResponseModel(
                    message=HTTPResponses.ITEM_NOT_FOUND().message,
                    status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
                )
            else:
                return HttpResponseModel(
                        message=HTTPResponses.ITEM_FOUND().message,
                        status_code=HTTPResponses.ITEM_FOUND().status_code,
                        data=room,
                    )
        else:
           return HttpResponseModel(
                    message=HTTPResponses.WITHOUT_ACESS().message,
                    status_code=HTTPResponses.WITHOUT_ACESS().status_code,
            ) 

    @staticmethod
    def add_promotion(promotion_request: PromotionModel) -> HttpResponseModel:
        """Add promotion in hotel method implementation"""
        if db.check_if_key_is_adm(promotion_request.adm_key):
            if promotion_request.discountValue > 0 and promotion_request.discountValue <= (promotion_request.reservationValue * 0.5) and promotion_request.discountValue != None:
                item = db.insert_promotion('promotions', promotion_request.dict(), promotion_request.room_id)
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
                    message=HTTPResponses.WITHOUT_ACESS().message,
                    status_code=HTTPResponses.WITHOUT_ACESS().status_code,
            )
        
    @staticmethod
    def update_promotion(promotion_request: PromotionUpdateModel) -> HttpResponseModel:
        """Update promotion in hotel method implementation"""
        if db.check_if_key_is_adm(promotion_request.adm_key):
            hotel_discount = db.find_hotel_by_room_id(promotion_request.room_id)["reservationValue"]
            if not hotel_discount:
                return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_FOUND().message,
                    status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
                )
            else:
                if promotion_request.newDiscountValue > 0 and promotion_request.newDiscountValue <= (hotel_discount * 0.5) and promotion_request.newDiscountValue != None:
                    item = db.update_promotion(promotion_request.room_id, promotion_request.newDiscountValue)
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
                    message=HTTPResponses.WITHOUT_ACESS().message,
                    status_code=HTTPResponses.WITHOUT_ACESS().status_code,
            )
        
    @staticmethod
    def delete_promotion(key: str, room_id: str) -> HttpResponseModel:
        """Delete a promotion in hotel method implementation"""
        if db.check_if_key_is_adm(key):
            hotel_discount = db.find_hotel_by_room_id(room_id)
            if not hotel_discount:
                return HttpResponseModel(
                    message=HTTPResponses.PROMOTION_NOT_FOUND().message,
                    status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
                )
            else:
                hotel_discount["_id"] = str(hotel_discount["_id"])
                hotel_removed = db.delete_promotion(hotel_discount["room_id"])
                return HttpResponseModel(
                            message=HTTPResponses.PROMOTION_DELETED().message,
                            status_code=HTTPResponses.PROMOTION_DELETED().status_code,
                            data=hotel_removed,
                        )
        else:
            return HttpResponseModel(
                    message=HTTPResponses.WITHOUT_ACESS().message,
                    status_code=HTTPResponses.WITHOUT_ACESS().status_code,
            )