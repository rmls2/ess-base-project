Feature: Review API

Scenario: Get review by ID successfully
Given the ReviewService return a review by id "0123" and user "Jorge Francisco"
When a "GET" request is send to "/review" and id "0123"
Then the response status should be "200"
And the JSON of the response must contain id "0123" and user "Jorge Francisco"

Scenario: Get review by ID unsuccessfully
Given there is no review by id "0123"
When a "GET" request is send to "/review" and id "0123"
Then the response status should be "404"
And the JSON of the response must be "Item not found"

Scenario: Creation of review successfully
Given the ReviewService register a review with the "quality" and "price" fields being mandatory
When a "POST" request is sent to "/register" with the "quality" "5" and "price" "4"
Then the response status should ne "200"
And the JSON of the response must be "Review criada"

Scenario: Creation of review unsuccessfully
Given the ReviewService register a review with the "quality" and "price" fields being mandatory
When a "POST" request is sent to "/register" without the field "quality"
Then the response status should ne "400"
And the JSON of the response must be "Review não criada"

Scenario: Update review successfully
Given the ReviewService update a review by id with "quality" or "price" fields being mandatory
And there is a review by id "0123" with "quality" "3" and "price" "5" 
When a "PUT" request is sent to "/update" with id "0123" with the "quality" "4" and "price" "5" 
Then the response status should be "200"
And the JSON of the response must be "Review atualizada"

Scenario: Update review unsuccessfully
Given the ReviewService update a review by id with "quality" or "price" fields being mandatory
And there is a review by id "0123" with "quality" "3" and "price" "5" 
When a "PUT" request is sent to "/update" with id "0123" with no "quality" or "price" field
Then the response status should be "400"
And the JSON of the response must be "Review não atualizada"

Scenario: Update not existing review
Given the ReviewService update a review by id with "quality" or "price" fields being mandatory
And there is no review by id "0123"
When a "PUT" request is sent to "/update"
Then the response status should be "400"
And the JSON of the response must be "Review não atualizada"

Scenario: Delete review successfully
Given the ReviewService deletes a review by id 
And There is a review by id "0123"
When a "DELETE" request is sent to "/delete" with id "0123"
The response status should be "200"
And the mensage must be "Review deletada"

Scenario: Delete review unsuccessfully
Given the ReviewService deletes a review by id
And there is no review by id "0123"
When a "DELETE" request is sent to "/delete" with iD "0123"
Then the response status should be "400"
And the mensage must be "Review não deletada"
