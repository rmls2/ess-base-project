from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.promotion_service import PromotionService
from src.tests.api.utils.utils import get_response_items_list, req_type_to_function

@scenario(
    scenario_name="Excluir uma promoção",
    feature_name="../features/promotions.feature"
)
def test_deletar_promocao():
    """ Delete a promotion"""
@given(parsers.cfparse('existe uma promoção com ID do quarto "{room_id}" e chave de administrador "{adm_key}"'), target_fixture="context")
def mock_promotion_delete_service_response(context, room_id: str, adm_key: bool):
    context["promotion_params"] = {
        "key": adm_key,
        "room_id": room_id
    }
    
    PromotionService.delete_promotion = lambda adm_key, room_id: HttpResponseModel(
        message=HTTPResponses.PROMOTION_DELETED().message,
        status_code=HTTPResponses.PROMOTION_DELETED().status_code,
        data={
            "room_id": room_id,
            "count": 1
        }
    )

    return context

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_delete_promotion(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.delete(req_url, params=context["promotion_params"])
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].json()["status_code"] == int(status_code)
    return context

@then(parsers.cfparse('o JSON da resposta deve indicar o sucesso com os elementos id do quarto "{room_id}" e o contador "{count}"'), target_fixture="context")
def check_response_data(context, room_id: str, count: int):
    """
    Check if the response data is the expected
    """
    expected_data = {
            "room_id": room_id,
            "count": int(count),
        }
    
    assert context["response"].json()["data"] == expected_data
    return context

