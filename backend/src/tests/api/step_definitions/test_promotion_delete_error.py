from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.promotion_service import PromotionService
from src.tests.api.utils.utils import get_response_items_list, req_type_to_function

@scenario(
    scenario_name="Usuario não autorizado a Excluir promoção",
    feature_name="../features/promotions.feature"
)
def test_usuario_nao_autorizado_a_deletar_promocao():
    """ Delete a promotion"""
@given(parsers.cfparse('existe uma promoção com ID do quarto "{room_id}" e chave de administrador "{adm_key}"'))
def mock_promotion_delete_service_response_error(room_id: str, adm_key: bool):
    global room_id_param
    global key_param

    room_id_param = room_id
    key_param = adm_key
    
    PromotionService.delete_promotion = lambda adm_key, room_id: HttpResponseModel(
        message=HTTPResponses.WITHOUT_ACESS().message,
        status_code=HTTPResponses.WITHOUT_ACESS().status_code,
        data=None
    )

@when(
    parsers.cfparse('uma requisição "{req_type}" é enviada para "{req_url}"'), 
    target_fixture="context"
)
def send_delete_promotion_error(client, context, req_type: str, req_url: str):
    """
    Send a request to the given URL using the given request type
    """

    response = client.delete(req_url, params={"key": key_param, "room_id": room_id_param})
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_response_error_status_code(context, status_code: str):
    """
    Check if the response status code is the expected
    """

    assert context["response"].json()["status_code"] == int(status_code)
    return context