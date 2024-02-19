from src.schemas.response import HttpResponseModel, HTTPResponses
from src.service.meta.review_service_meta import ReviewServiceMeta
from src.db.__init__ import database as db
from src.schemas.reviews import ReviewModel, ReviewUpdateModel, ReviewDeleteModel

class ReviewService(ReviewServiceMeta):
    @staticmethod
    def get_review(review_id: str) -> HttpResponseModel:
        """Get review by review id method implementation"""
        item = db.get_item_by_review_id('reviews', review_id)
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
    def add_review(review_request: ReviewModel) -> HttpResponseModel:
        """Add review in attraction method implementation"""
        item = db.insert_review('Reviews', review_request.model_dump())
        if not item:
                return HttpResponseModel(
                    message=HTTPResponses.REVIEW_NOT_CREATED().message,
                    status_code=HTTPResponses.REVIEW_NOT_CREATED().status_code,
                )
        item["_id"] = str(item["_id"])
        return HttpResponseModel(
                message=HTTPResponses.REVIEW_CREATED().message,
                status_code=HTTPResponses.REVIEW_CREATED().status_code,
                data=item,
            )
        

    @staticmethod
    def update_review(review_request: ReviewUpdateModel) -> HttpResponseModel:
        """Update review in attraction method implementation"""
        quality = db.find_review_by_name(review_request.attraction, review_request.user)["quality"]
        price = db.find_review_by_name(review_request.attraction, review_request.user)["price"]
        if not quality or not price:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        else:
            item = db.update_review(review_request.attraction, review_request.user, review_request.newQuality, review_request.newPrice)
            if not item:
                return HttpResponseModel(
                    message=HTTPResponses.REVIEW_NOT_UPDATED().message,
                    status_code=HTTPResponses.REVIEW_NOT_UPDATED().status_code,
                )
            item["_id"] = str(item["_id"])
            return HttpResponseModel(
                    message=HTTPResponses.REVIEW_UPDATED().message,
                    status_code=HTTPResponses.REVIEW_UPDATED().status_code,
                    data=item,
                ) 
    
    @staticmethod
    def delete_review(review_request: ReviewDeleteModel) -> HttpResponseModel:
        """Delete a review in attraction method implementation"""
        review = db.find_hotel_by_name(review_request.attraction, review_request.user)
        if not review:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        else:
            review["_id"] = str(review["_id"])
            review_removed = db.delete_review(review["attraction"], review["user"])
            return HttpResponseModel(
                        message=HTTPResponses.REVIEW_DELETED().message,
                        status_code=HTTPResponses.REVIEW_DELETED().status_code,
                        data=review_removed,
                    )