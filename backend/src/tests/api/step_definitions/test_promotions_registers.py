from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.promotion_service import PromotionService
from src.tests.api.utils.utils import get_response_items_list, req_type_to_function

@scenario(
    scenario_name="Registrar uma nova promoção",
    feature_name="../features/promotions.feature"
)
def test_registrar_promocao():
    """ Register new promotion"""
@given(parsers.cfparse('o PromotionService retorna um documento de promoção user "{user_name}", adm_key "{adm_key}", hotel "{hotel_name}", room_id "{room_id}", reservationValue "{reservation_value}", discountValue "{discount_value}" e id "{promotion_id}"'), target_fixture="context")
def mock_promotion_service_response(context, user_name: str, adm_key: str, hotel_name: str, room_id: str, reservation_value: float, discount_value: float, promotion_id: str):
    """
    Mock the PromotionService.get_current_discount_value() method to return a current discount with the given room_id
    """
    context["promotion_request"] = {
        "_id": promotion_id,
        "user": user_name,
        "adm_key": adm_key,
        "hotel": hotel_name,
        "room_id": room_id,
        "reservationValue": reservation_value,
        "discountValue": discount_value,
    }


    PromotionService.add_promotion = lambda model: HttpResponseModel(
        message=HTTPResponses.PROMOTION_CREATED().message,
        status_code=HTTPResponses.PROMOTION_CREATED().status_code,
        data=context["promotion_request"]
    )

    return context

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_add_promotion(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.post(req_url, json=context["promotion_request"])
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve indicar o sucesso com o documento user "{user_name}", adm_key "{adm_key}", hotel "{hotel_name}", room_id "{room_id}", reservationValue "{reservation_value}", discountValue "{discount_value}" e id "{promotion_id}"'), target_fixture="context")
def check_response_data(context, user_name: str, adm_key: str, hotel_name: str, room_id: str, reservation_value: float, discount_value: float, promotion_id: str):
    """
    Check if the response data is the expected
    """
    expected_data = {
            "_id": promotion_id,
            "user": user_name,
            "adm_key": adm_key,
            "hotel": hotel_name,
            "room_id": room_id,
            "reservationValue": reservation_value,
            "discountValue": discount_value,
        }
    
    assert context["response"].json()["data"] == expected_data
    return context


@scenario(
    scenario_name="Tentar registrar uma nova promoção com discountValue negativo",
    feature_name="../features/promotions.feature"
)
def test_tentar_registrar_valor_negativo():
    "Try to register a promotion with negative value"

@given(parsers.cfparse('a solicitação para registrar uma nova promoção é inválida com o request: user "{user_name}", adm_key "{adm_key}", hotel "{hotel_name}", room_id "{room_id}", reservationValue "{reservation_value}", discountValue "{discount_value}"'), target_fixture="context")
def mock_promotion_service_error_response(context, user_name: str, adm_key: str, hotel_name: str, room_id: str, reservation_value: float, discount_value: float):
    context["promotion_request"] = {
        "user": user_name,
        "adm_key": adm_key,
        "hotel": hotel_name,
        "room_id": room_id,
        "reservationValue": reservation_value,
        "discountValue": discount_value,
    }
    PromotionService.add_promotion = lambda model: HttpResponseModel(
        message=HTTPResponses.PROMOTION_NOT_CREATED().message,
        status_code=HTTPResponses.PROMOTION_NOT_CREATED().status_code,
        data=None
    )
    
    return context

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_add_promotion_negative_value_request(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.post(req_url, json=context["promotion_request"])
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code_negative_value(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve conter a mensagem de erro "{error_msg}"'), target_fixture="context")
def check_error_msg(context, error_msg: str):
    assert context["response"].json()["message"] == error_msg
    return context
