Feature: Review API

Scenario: Get review by ID 
Given the ReviewService return a review by id "0123" and user "Jorge Francisco"
When a "GET" review_request is send to "/review/0123"
Then the response status should be "201"
And the JSON of the response must contain id "0123" and user "Jorge Francisco"

Scenario: Creation of review unsuccessfully
Given the ReviewService register a review with the "quality" and "price" fields being mandatory
When a "POST" review_request is sent to "/register" without the field "quality"
Then the response status should ne "400"
And the JSON of the response must be Review não criada"

Scenario: Creation of review successfully
Given the ReviewService register a review with the "quality" and "price" fields being mandatory
When a "POST" review_request is sent to "/register" with the "quality" "5" and "price" "4"
Then the response status should ne "200"
And the JSON of the response must be "Review criada"

Scenario: Update review successfully
Given the ReviewService update a review by id with "quality" or "price" fields being mandatory
And the review by id "0123" with "quality" "3" and "price" "5" 
When a "PUT" review_request is sent to "/update" with id "0123"
And the "new_quality" is "4" and "new_price" is "5" 
Then the response status should be "200"
And the mensage must be "Successfully updated review"
And the JSON of the response must contain id "0123" with "quality" "4" and "price" "5"

Scenario: Update review unsuccessfully
Given the ReviewService update a review by id with "quality" or "price" fields being mandatory
And the review by id "0123" and user "Jorge Francisco" with "quality" "3" and "price" "5" 
When a "PUT" review_request is sent to "/update" with id "0123" with no "quality" or "price" field
Then the response status should be "400"
And the mensage must be "Invalid request"

Scenario: Delete review
Given the ReviewService deletes a review by id 
When a "DELETE" review_request is sent to "/delete" with id "0123"
The response status should be "200"
And the mensage must be "Successfully deleted review"
