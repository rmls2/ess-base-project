from src.schemas.response import HTTPResponses, HttpResponseModel
from pytest_bdd import parsers, given, when, then, scenario
from src.service.impl.review_service import ReviewService
import pytest
from src.schemas.reviews import ReviewDeleteModel

""" Scenario: Get review by ID successfully """

@scenario(scenario_name="Get review by ID successfully", feature_name="../features/review-service.feature")
def test_service_get_review():
    """ Get review by ID successfully """

# Step definitions for the "Obter item por ID" scenario
@given(parsers.cfparse(
    'the ReviewService return a review by id "{review_id}"'))
def mock_review_service(review_id: str):
    """
    Mock the ReviewService.get_review() method to return an item with the given id and name
    """

    ReviewService.get_review = lambda id : HttpResponseModel(
        message=HTTPResponses.ITEM_FOUND().message,
        status_code=HTTPResponses.ITEM_FOUND().status_code,
        data={"id": review_id}
    )

@when(
    parsers.cfparse('a GET request is send to /review and id "{review_id}"'), 
    target_fixture="context"
)
def get_review(context, review_id: str):
    context['review'] = ReviewService.get_review(review_id)
    return context

@then(
    parsers.cfparse('the response status should be "{status_response}"'), 
    target_fixture="context"
)
def check_received_item(context, status_response: int):
    assert context['review'].status_code == int(status_response)
    return context

# Mudar cénario e esse código para apenas receber a mensagem e não dados
@then(
    parsers.cfparse('the JSON of the response must be "{message}"'), 
    target_fixture="context"
)
def check_received_item(context, message: str):
    assert context['review'].message == message
    return context

# Mudar cénario e esse código para apenas receber a mensagem e não dados
@then(
    parsers.cfparse('the review returned must contain user "{review_user}" attraction "{review_attraction}" quality "{review_quality}" and price "{review_price}"'), 
    target_fixture="context"
)
def check_received_item(context, review_user: str, review_attraction: str, review_quality: int, review_price: int):
    assert context['review'].data.user == review_user
    assert context['review'].data.attraction == review_attraction
    assert context['review'].data.quality == review_quality
    assert context['review'].data.price == review_price
    return context


""" Scenario: Get review by ID unsuccessfully """
@scenario(scenario_name="Get review by ID unsuccessfully", feature_name="../features/review-service.feature")
def test_service_get_review():
    """ Get review by ID unsuccessfully """    

# Step definitions for the "Obter item por ID" scenario
@given(parsers.cfparse(
    'the ReviewService does not return a nonexistent review by id "{review_id}"'))
def mock_review_service(review_id: str):
    ReviewService.get_review = lambda id : HttpResponseModel(
        message=HTTPResponses.ITEM_NOT_FOUND().message,
        status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
    )

@when(
    parsers.cfparse('a GET request is send to /review and id "{review_id}"'), 
    target_fixture="context"
)
def get_review(context, review_id: str):
    context['review'] = ReviewService.get_review(review_id)
    return context

@then(
    parsers.cfparse('the response status should be "{status_response}"'), 
    target_fixture="context"
)
def check_received_item(context, status_response: int):
    assert context['review'].status_code == int(status_response)
    return context

@then(
    parsers.cfparse('the JSON of the response must be "{message}"'), 
    target_fixture="context"
)
def check_received_item(context, message: str):
    assert context['review'].message == message
    return context

""" Scenario: Creation of review successfully """

@scenario(scenario_name="Creation of review successfully", feature_name="../features/review-service.feature")
def test_service_add_review():
    """ Creation of review successfully """

# Step definitions for the "Obter item por ID" scenario
@given(parsers.cfparse(
        'the ReviewService register a review with the user "{review_user}" attraction "{review_attraction}" quality "{review_quality}" and price "{review_price}" fields being mandatory'))
def mock_review_service(review_user:str, review_attraction: str, review_quality: int, review_price: int):
    """
    Mock the ItemService.add_review() method to return an item with the given id and name
    """

    ReviewService.add_review = lambda id : HttpResponseModel(
        message=HTTPResponses.REVIEW_CREATED().message,
        status_code=HTTPResponses.REVIEW_CREATED().status_code,
        data={"user": review_user, "attraction": review_attraction, "quality": review_quality, "price": review_price}
    )

@when(
    parsers.cfparse('a POST request is sent to /register with the user "{review_user}" attraction "{review_attraction}" quality "{review_quality}" and price "{review_price}"'), 
    target_fixture="context"
)
def add_review(context, review_user:str, review_attraction: str, review_quality: int, review_price: int):
    context['review'] = ReviewService.add_review({review_user, review_attraction, review_quality, review_price})
    return context

@then(
    parsers.cfparse('the response status should be "{status_response}"'), 
    target_fixture="context"
)
def check_received_item(context, status_response: int):
    assert context['review'].status_code == int(status_response)
    return context

@then(
    parsers.cfparse('the JSON of the response must be "{message}"'), 
    target_fixture="context"
)
def check_received_item(context, message: int):
    assert context['review'].message == message
    return context

@pytest.fixture
def review_id():
    return "0123"  

@pytest.fixture
def review_user():
    return "Jorge Francisco"  

@pytest.fixture
def review_attraction():
    return "template"

@pytest.fixture
def review_quality():
    return "4"

@pytest.fixture
def review_price():
    return "2"

""" Scenario: Update review successfully """
@pytest.mark.usefixtures('review_user', 'review_attraction', 'review_quality', 'review_price')
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Update review successfully", feature_name="../features/review-service.feature")
def test_service_update_review():
    """ Update review successfully """

# Step definitions for the "Obter item por ID" scenario
@given(parsers.cfparse(
    'the ReviewService update a review with name "{review_user}" attraction "{review_attraction}" newQuality "{review_quality}" and/or newPrice "{review_price}"'))
def mock_review_service(review_user: str, review_attraction: str, review_quality: int, review_price: int):

    ReviewService.update_review = lambda id : HttpResponseModel(
        message=HTTPResponses.REVIEW_UPDATED().message,
        status_code=HTTPResponses.REVIEW_UPDATED().status_code,
        data={"user": review_user, "attraction": review_attraction, "quality": review_quality, "price": review_price}
    )

@when(
    parsers.cfparse('a PUT request is sent to /update with user "{review_user}" attraction "{review_attraction}" newQuality "{review_quality}" and newPrice "{review_price}"'), 
    target_fixture="context"
)
def update_review(context, review_user:str, review_attraction: str, review_quality: int, review_price: int):
    context['review'] = ReviewService.update_review({review_user, review_attraction, review_quality, review_price})
    return context

@then(
    parsers.cfparse('the response status should be "{status_response}"'), 
    target_fixture="context"
)
def check_received_item(context, status_response: int):
    assert context['review'].status_code == int(status_response)
    return context

# Mudar cénario e esse código para apenas receber a mensagem e não dados
@then(
    parsers.cfparse('the JSON of the response must be "{message}"'), 
    target_fixture="context"
)
def check_received_item(context, message: int):
    assert context['review'].message == message
    return context



""" Scenario: Delete review successfully """
@pytest.mark.usefixtures("review_id")
# This method is used to define the scenario name and feature file path
@scenario(scenario_name="Delete review successfully", feature_name="../features/review-service.feature")
def test_service_update_review():
    """ Delete review successfully  """

@given(parsers.cfparse(
    'the ReviewService deletes a review by id "{review_id}"'))
def mock_review_service(review_id: str):
    """
    Mock the ItemService.get_item() method to return an item with the given id and name
    """

    ReviewService.update_review = lambda id : HttpResponseModel(
        message=HTTPResponses.REVIEW_DELETED().message,
        status_code=HTTPResponses.REVIEW_DELETED().status_code,
        data={"review_is": review_id}
    )

@when(
    parsers.cfparse('a DELETE request is sent to /delete with id "{review_id}"'), 
    target_fixture="context"
)
def add_review(context, review_id: str):
    context['review'] = ReviewService.delete_review(ReviewDeleteModel(review_id))
    return context

@then(
    parsers.cfparse('the response status should be "{status_response}"'), 
    target_fixture="context"
)
def check_received_item(context, status_response: int):
    assert context['review'].status_code == int(status_response)
    return context

# Mudar cénario e esse código para apenas receber a mensagem e não dados
@then(
    parsers.cfparse('the JSON of the response must be "{message}"'), 
    target_fixture="context"
)
def check_received_item(context, message: int):
    assert context['review'].message == message
    return context

