from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.promotion_service import PromotionService
from src.tests.api.utils.utils import get_response_items_list, req_type_to_function

@scenario(
    scenario_name="Atualizar uma promoção existente",
    feature_name="../features/promotions.feature"
)
def test_atualizar_promocao():
    """Update promotion"""
@given(parsers.cfparse('existe uma promoção com ID do quarto "{room_id}" e a requisição tem user "{user_name}", adm_key "{adm_key}", currentDiscountValue "{current_discount_value}", newDiscountValue  "{new_discount_value}"'))
def mock_promotion_service_response_update(context, room_id: str, user_name: str, adm_key: str, current_discount_value: float, new_discount_value: float):
    context["promotion_request"] = {
        "user": user_name,
        "adm_key": adm_key,
        "room_id": room_id,
        "currentDiscountValue": current_discount_value,
        "newDiscountValue": new_discount_value,
    }

    PromotionService.update_promotion = lambda model: HttpResponseModel(
        message=HTTPResponses.PROMOTION_UPDATED().message,
        status_code=HTTPResponses.PROMOTION_UPDATED().status_code,
        data= {
          "_id": "65d26a97e24aa3a20694e3aa",
          "user": user_name,
          "adm_key": adm_key,
          "hotel": "noite estrelada",
          "room_id": room_id,
          "reservationValue": 150.0,
          "discountValue": 20.0
        }
    )
    
    return context

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_update_promotion(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.put(req_url, json=context["promotion_request"])
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
            "reservationValue": float(reservation_value),
            "discountValue": float(discount_value),
        }
    
    assert context["response"].json()["data"] == expected_data
    return context


@scenario(
    scenario_name="Tentar atualizar uma promoção inexistente",
    feature_name="../features/promotions.feature"
)
def test_falha_ao_atualizar_promocao():
    """Update promotion"""
@given(parsers.cfparse('não existe uma promoção com ID do quarto "{room_id}" e a requisição tem user "{user_name}", adm_key "{adm_key}", currentDiscountValue "{current_discount_value}", newDiscountValue  "{new_discount_value}"'))
def mock_promotion_service_response_update_error(context, room_id: str, user_name: str, adm_key: str, current_discount_value: float, new_discount_value: float):
    context["promotion_request"] = {
        "user": user_name,
        "adm_key": adm_key,
        "room_id": room_id,
        "currentDiscountValue": current_discount_value,
        "newDiscountValue": new_discount_value,
    }

    PromotionService.update_promotion = lambda model: HttpResponseModel(
        message=HTTPResponses.PROMOTION_NOT_FOUND().message,
        status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
        data= None
    )
    
    return context

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_update_promotion(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.put(req_url, json=context["promotion_request"])
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_error_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve conter a mensagem de erro "{error_msg}"'), target_fixture="context")
def check_response_data(context, error_msg: str):
    """
    Check if the response data is the expected
    """
    
    assert context["response"].json()["message"] == error_msg
    return context