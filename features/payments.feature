Feature: Payments
	As a user looking to buy a host travel services
	I want to add and modify methods of payment
	So that I can buy service by payment methods using a payment method registered

Scenario: overview of my cards
	Given I am at the "pagamentos" page
	when I select "meus cartões" option
	then I can see "meus cartões" page

Scenario: adding a new card (payment method)
	Given I am at the "meus cartões" page
	When I select "+" option
	Then I am at "cadastro de cartão" page

Scenario: registering info about a new card (payment method)
	Given I am at the "cadastro de cartão" page
	When I add fill nome de cartão "Higgins claudiano" 
	And I add fill numero de cartão "1234123412341234"
	And I add fill data de validade "12/29"
	And I add fill código de segurança (cvv) "000"
	And I select "débito" option
	Then I "Save" the information
	And I can see a message of "Sucesso"