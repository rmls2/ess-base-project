from typing import Optional
from pydantic import BaseModel

class HttpResponseModel(BaseModel):
    message: str
    status_code: int
    data: Optional[dict] | Optional[list] = None

class HTTPResponses:

    """
    This class contains the basic HTTP responses for the API
    """

    @staticmethod
    def WITHOUT_ACESS() -> HttpResponseModel:
        return HttpResponseModel(
            message="User don't have acess",
            status_code=401,
        )

    @staticmethod
    def ITEM_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item not found",
            status_code=404,
        )

    @staticmethod
    def ITEM_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item found",
            status_code=200,
        )

    @staticmethod
    def ROOM_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Room not found",
            status_code=404,
        )

    @staticmethod
    def ROOM_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Room found",
            status_code=200,
        )

    @staticmethod
    def ITEM_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item created",
            status_code=201,
        )
    
    @staticmethod
    def PROMOTION_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion not found",
            status_code=404,
        )

    @staticmethod
    def PROMOTION_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion found",
            status_code=200,
        )
    
    @staticmethod
    def PROMOTION_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion created",
            status_code=201,
        )
    
    @staticmethod
    def REVIEW_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review criada",
            status_code=201,
        )

    @staticmethod
    def PROMOTION_NOT_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion not created",
            status_code=422,
        )
    
    @staticmethod
    def PROMOTION_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion updated",
            status_code=200,
        )

    def REVIEW_NOT_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review não criada",
            status_code=400,
        )
    
    @staticmethod
    def REVIEW_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review atualizada",
            status_code=200,
        )

    @staticmethod
    def PROMOTION_NOT_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion not updated",
            status_code=422,
        )
    
    @staticmethod
    def PROMOTION_DELETED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Promotion deleted",
            status_code=200,
        )

    def REVIEW_NOT_UPDATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review não atualizada",
            status_code=400,
        )

    @staticmethod
    def REVIEW_DELETED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review deletada",
            status_code=200,
        )

    @staticmethod
    def REVIEW_NOT_DELETED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review não deletada",
            status_code=400,
        )

    @staticmethod
    def SERVER_ERROR() -> HttpResponseModel:
        return HttpResponseModel(
            message="Server error",
            status_code=500,
        )


    # TODO: implement other responses (item created, updated, deleted, etc)