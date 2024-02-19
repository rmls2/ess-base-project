from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.promotion_service import PromotionService
from src.tests.api.utils.utils import get_response_items_list, req_type_to_function

@scenario(
    scenario_name="Obter uma promoção por ID do quarto",
    feature_name="../features/promotions.feature"
)
def test_obter_promocao_por_id_do_quarto():
    """ Get promotion by room ID"""

@given(parsers.cfparse('o PromotionService retorna os valores de uma promoção com reservationValue "{reservation_value}" e newValue "{new_value}"'))
def mock_promotion_service_response(reservation_value: float, new_value: float):
    """
    Mock the PromotionService.get_promotion() method to return a promotion with the given room_id and values
    """
    PromotionService.get_promotion = lambda id: HttpResponseModel(
        message=HTTPResponses.PROMOTION_FOUND().message,
        status_code=HTTPResponses.PROMOTION_FOUND().status_code,
        data={"reservationValue": reservation_value, "newValue": new_value}
    )

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_get_promotion_request(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """
    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(
    parsers.cfparse('o JSON da resposta deve conter reservationValue "{reservation_value}" e newValue "{new_value}"'), 
    target_fixture="context"
)
def check_response_json_contains_promotion_data(context, reservation_value: float, new_value: float):
    """
    Check if the response JSON contains the promotion reservationValue and newValue
    """
    expected_data = {"reservationValue": reservation_value, "newValue": new_value}
    assert context["response"].json()["data"] == expected_data
    return context


@scenario(
    scenario_name="Obter o valor atual de desconto por ID do quarto",
    feature_name="../features/promotions.feature"
)
def test_obter_desconto_atual_quarto():
    """ Get current discount by room ID"""

@given(parsers.cfparse('o PromotionService retorna id da promoção "{promotion_id}" e valor atual de desconto "{current_discount}"'))
def mock_promotion_service_response_discount(promotion_id: str, current_discount: float):
    """
    Mock the PromotionService.get_current_discount_value() method to return a current discount with the given room_id
    """
    PromotionService.get_current_discount_value = lambda id: HttpResponseModel(
        message=HTTPResponses.PROMOTION_FOUND().message,
        status_code=HTTPResponses.PROMOTION_FOUND().status_code,
        data={"id": promotion_id, "currentValue": current_discount}
    )

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_get_current_discount_value_request(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """
    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(
    parsers.cfparse('o JSON da resposta deve conter o valor atual de desconto "{current_discount}" e id da promoção "{promotion_id}"'), 
    target_fixture="context"
)
def check_current_response_error_msg(context, promotion_id: str, current_discount: float):
    """
    Check if the response message is the expected
    """
    expected_data = {"id": promotion_id, "currentValue": current_discount}
    assert context["response"].json()["data"] == expected_data
    return context

@scenario(
    scenario_name="Registrar uma nova promoção",
    feature_name="../features/promotions.feature"
)
def test_registrar_promocao():
    """ Register new promotion"""
@given(parsers.cfparse('o PromotionService retorna um documento de promoção user "{user_name}", adm "{adm_tag}", hotel "{hotel_name}", room_id "{room_id}", reservationValue "{reservation_value}", discountValue "{discount_value}" e id "{promotion_id}"'))
def mock_promotion_service_response(user_name: str, adm_tag: bool, hotel_name: str, room_id: str, reservation_value: float, discount_value: float, promotion_id: str):
    """
    Mock the PromotionService.get_current_discount_value() method to return a current discount with the given room_id
    """
    PromotionService.add_promotion = lambda id : HttpResponseModel(
        message=HTTPResponses.PROMOTION_CREATED().message,
        status_code=HTTPResponses.PROMOTION_CREATED().status_code,
        data={
            "id": promotion_id,
            "user": user_name,
            "adm": adm_tag,
            "hotel": hotel_name,
            "room_id": room_id,
            "reservationValue": reservation_value,
            "discountValue": discount_value,
        }
    )

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_add_promotion(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].status_code == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve indicar o sucesso com o documento user "{user_name}", adm "{adm_tag}", hotel "{hotel_name}", room_id "{room_id}", reservationValue "{reservation_value}", discountValue "{discount_value}" e id "{promotion_id}"'), target_fixture="context")
def check_response_status_code(context, user_name: str, adm_tag: bool, hotel_name: str, room_id: str, reservation_value: float, discount_value: float, promotion_id: str):
    """
    Check if the response data is the expected
    """
    expected_data = {
            "id": promotion_id,
            "user": user_name,
            "adm": adm_tag,
            "hotel": hotel_name,
            "room_id": room_id,
            "reservationValue": reservation_value,
            "discountValue": discount_value,
        }
    
    assert context["response"].json()["data"] == expected_data
    return context

@scenario(
    scenario_name="Tentar obter uma promoção inexistente por ID do quarto",
    feature_name="../features/promotions.feature"
)
def test_obter_promocao_por_id_do_quarto_nao_existente():
    """ Get promotion by room ID that not exists"""

@given(parsers.cfparse('não existe uma promoção com ID do quarto "{room_id}"'))
def mock_promotion_service_response_not_found(room_id: str):
    """
    Mock the PromotionService.get_promotion() method to return a promotion not found with the given room_id
    """
    PromotionService.get_promotion = lambda id: HttpResponseModel(
        message=HTTPResponses.PROMOTION_NOT_FOUND().message,
        status_code=HTTPResponses.PROMOTION_NOT_FOUND().status_code,
        data=None
    )

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_get_promotion_request_not_found(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """
    response = req_type_to_function(client, req_type)(req_url)
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """
    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(
    parsers.cfparse('o JSON da resposta deve conter a mensagem de erro "{error_msg}"'), 
    target_fixture="context"
)
def check_get_response_error_msg(context, error_msg: str):
    """
    Check if the response message is the expected
    """
    assert context["response"].json()["message"] == error_msg
    return context
