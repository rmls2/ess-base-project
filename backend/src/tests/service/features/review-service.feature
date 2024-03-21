Feature: Review API

Scenario: Get review by ID successfully
Given the ReviewService return a review by id "0123"
When a GET request is send to /review and id "0123"
Then the response status should be "200"
And the JSON of the response must be "Item found"
And the review returned must contain user "Jorge Francico" attraction "template" quality "5" and price "4"

Scenario: Get review by ID unsuccessfully
Given the ReviewService does not return a nonexistent review by id "0123" 
When a GET request is send to /review and id "0123"
Then the response status should be "404"
And the JSON of the response must be "Item not found"

Scenario: Creation of review successfully
Given the ReviewService register a review with the user "Jorge Francisco" attraction "template" quality "5" and price "5" fields being mandatory
When a POST request is sent to /register with the user "Jorge Francisco" attraction "template" quality "5" and price "5"
Then the response status should be "201"
And the JSON of the response must be "Review criada"

Scenario: Update review successfully
Given the ReviewService update a existing review with user "Jorge Francisco" attraction "template" newQuality "4" and/or newPrice "2"
When a PUT request is sent to /update with user "Jorge Francisco" attraction "template" newQuality "5" and newPrice "5"
Then the response status should be "200"
And the JSON of the response must be "Review atualizada"

Scenario: Delete review successfully
Given the ReviewService deletes a review by id "0123"
When a DELETE request is sent to /delete with id "0123"
The response status should be "200"
And the mensage must be "Review deletada"
