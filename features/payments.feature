Feature: Payments
	As a user looking to buy a host travel services
	I want to add and modify methods of payment
	so that I can buy service by payment methods using a payment method registered

Scenario: overview of my cards
	Given I am at the "pagamentos" page
	When I select "meus cartões" option
	Then I can see "meus cartões" page

Scenario: overview of transaction history
	Given I am at the "pagamentos" page
	when I select "histórico de transações" option
	then I can see "histórico de transações" page

Scenario: adding a new card (payment method)
	Given I am at the "meus cartões" page
	When I select "+" option
	Then I am at "cadastro de cartão" page

Scenario: editing a card (payment method)
	Given I am at the "meus cartões" page
	When I select "pen" option at "cartão_1"
	Then I am at "edição de cartão" page

Scenario: editing info of a card (payment method) 
	Given I am at the "edição de cartão" page
	When I erase nome de cartão "Higgins claudiano" 
	Then I "Save" the information
	And I can see a message of "Informações incompletas" there is not a valid "nome de cartão"

Scenario: registering info about a new card (payment method) 
	Given I am at the "cadastro de cartão" page
	When I add fill nome de cartão "Higgins claudiano" 
	And I add fill numero de cartão "1234123412341234"
	And I add fill data de validade "12/29"
	And I add fill código de segurança (cvv) "000"
	And I select "débito" option
	Then I "Save" the information
	And I can see a message of "Sucesso"

Scenario: registering info about a new card (payment method) [incompleto]
	Given I am at the "cadastro de cartão" page
	When I add fill nome de cartão "Higgins claudiano" 
	And I add fill numero de cartão "1234123412341234"
	And I add fill data de validade "12/29"
	And I select "débito" option
	Then I "Save" the information
	And I can see a message of "Informações incompletas" there is not a valid "codigo de segurança" 

Scenario: Transaction history of a card
	Given I am at the "Historico de transações" page
	when I select a card "cartão1" 
	then I can see the history of the card "Historico cartão1" page

