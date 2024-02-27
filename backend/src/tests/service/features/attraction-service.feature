Feature: Attractions Service

Scenario: Get attraction by id
Given the AttractionService return a attraction by id "123" and name "Atração 1" 
When a "GET" request is send to "/attraction/123"
Then response status should be "200"
And the JSON of the response must contain id "123" and name "Atração 1"

Scenario: Get all images from attraction
Given the AttractionService return a list of images
When a "GET" request is send to "/attraction/123/get_images"
Then response status should be "200"
And the JSON of the response must be a list of images
And ...  # exemplo: o item com id "123" e nome "Exemplo de Item" está na lista
And ...

Scenario: Get all reviews from attraction
Given the AttractionService return a list of reviews
When a "GET" request is send to "/attraction/123/get_reviews"
Then response status should be "200"
And the JSON of the response must be a list of reviews
And the review by id "0123" and user "Jorge Francisco" must be in the list
And the review by id "0124" and user "José Silva" must be in the list

Scenario: Make reservation ?
Given ...
When ...
Then ...
