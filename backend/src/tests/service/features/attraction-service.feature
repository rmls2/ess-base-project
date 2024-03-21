Feature: Attractions Service

Scenario: Get attraction by id
Given the AttractionService return a attraction by id "123" and name "Atração 1" 
When a "GET" request is send to "/attraction/123"
Then response status should be "200"
And the JSON of the response must contain a attraction by id "123" and name "Atração 1"

Scenario: Get attraction by id unsuccessfully
Given there is no Attraction by id "123"
When a "GET" request is send to "/attraction/123"
Then the response status should be "404"
And the JSON of the response must be "Item not found"

Scenario: Get all images from attraction
Given the AttractionService return a list of images
When a "GET" request is send to "/attraction/123/get_images"
Then response status should be "200"
And the JSON of the response must contain a list of images

Scenario: Get all reviews from attraction
Given the AttractionService return a list of reviews
When a "GET" request is send to "/attraction/123/get_reviews"
Then response status should be "200"
And the JSON of the response must be a list of reviews

Scenario: Make reservation ?
Given ...
When ...
Then ...
