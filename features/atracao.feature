Feature: attraction
As a System User
I want to view detailed information about an attraction
so that I can assess whether it is worth booking the attraction

Scenario: view all photos
Given I'm on the "attraction" page
And I can see 2 photos about the attraction
When I select "more photos"
Then I'm still on the "attraction" page
And I can see 5 photos about the "attraction"

Scenario: See all reviews
Given I'm on the "attraction" page
And I can see 3 reviews with the ratings “8.63”, “8.63 and “9”
When I select "see all reviews"
Then I'm still on the "attraction" page
And I can see 5 reviews with the ratings “8.63”, ”8.63”, “9”, 6.67” and “8”

Scenario: Select related attraction
Given I'm on the "attraction" page
And I can see the name "As Coloridas" and the zip code "55870000"
When I select the attraction "Aconchego Familiar-Piscina Privativa" in "similar attractions"
Then I am redirected to the "attraction" page
And I can see the name "Aconchego Familiar-Piscina Privativa" and the zip code "55870000"

Scenario: Make reservation
Given I'm on the "attraction" page
And I can see the attraction "As Coloridas" with the attraction value "R$500.00"
When I select “Make a reservation”
Then I am redirected to the "payments" page
And I can see the name of the attraction "As Coloridas" with the value "R$500.00" in "Amount to pay"

Feature: Rate attraction
As a System User
I want to evaluate an attraction based on its characteristics
So that I can express my satisfaction about that attraction

Scenario: Rate attraction successfully
Given I am logged in as a customer with the name "Jorge Francisco"
And I'm on the "attraction page" with the name "Bate e volta para Campos do Jordão"
And I don't see the review "Evaluation by Jorge Francisco"
When I select "Rate Attraction"
And I put "4/5" in "Quality" and "3/5" in "Price"
And select "Finish review"
Then I can see the message "Avaliação preenchida corretamente"
And I'm still on the "Attraction Page"
And I can see the review "Evaluation by Jorge Francisco"
And I can see the ratings "4/5" under "Quality" and "3/5" under "Price"

Scenario: Rate attraction unsuccessfully
Given I am logged in as a customer with the name "Jorge Francisco"
And I'm on the "attraction page" with the name "Bate e volta para Campos do Jordão"
And I don't see the review "Evaluation by Jorge Francisco"
When I select "Rate Attraction"
And I put "4/5" in "Quality" and nothing in "Price"
And Select "Finish review"
Then I can see the message "Avaliação preenchida incorretamente"
And I'm still on the "Attraction Page"
And I don't see the review "Evaluation by Jorge Francisco"

Scenario: edit Rate attraction
Given I am logged in as a customer with the name "Jorge Francisco"
And I'm on the "attraction page" with the name "Bate e volta para Campos do Jordão"
And I see the review "Evaluation by Jorge Francisco"
And I can see the ratings "4/5" under "Quality" and "3/5" under "Price"
When I select "Edit review"
And I put "2/5" in "Quality" and "1/5" in "Price"
And Select "Finish review"
Then I can see the message "Avaliação editada"
And I'm still on the "Attraction Page"
And I can see the review "Evaluation by Jorge Francisco"
And I can see the ratings "2/5" under "Quality" and "1/5" under "Price"


Feature: Attractions API

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

Feature: Review API

Scenario: Get review by ID 
Given the ReviewService return a review by id "0123" and user "Jorge Francisco"
When a "GET" review_request is send to "/review/0123"
Then the response status should be "200"
And the JSON of the response must contain id "0123" and user "Jorge Francisco"

Scenario: Register review 
Given the ReviewService register a review by id 
When a "POST" review_request is sent to "/register" with id "0123"
Then the response status should ne "200"
And the JSON of the response must contain id "0123"

Scenario: Update review
Given the ReviewService update a review by id and user
And the review by id "0123" and user "Jorge Francisco" with "quality" "3" and "price" "5" 
When a "PUT" review_request is sent to "/update" with id "0123" and user "Jorge Francisco"
And the "new_quality" is "4" and "new_price" is "5" 
Then the response status should be "200"
And the JSON of the response must contain id "0123" with "quality" "4" and "price" "5"
