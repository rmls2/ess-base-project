Feature: Promotions
    As an administrator responsible for the payment system
    I want to manage payment methods and promotions
    So that I can facilitate transactions and provide benefits to users

Scenario: Successful Promotion Registration
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has no promotion
    When the user "Pedro" chooses "cadastrar promoção"
    And the user "Pedro" fills in the "valor promoção" field with a valid value
    And the user "Pedro" fills in the "data inicial - data final" field with valid dates
    And the user "Pedro" chooses "confirmar promoção"
    Then the user "Pedro" receives a message of "Promoção cadastrada com sucesso!"
    And the hotel "noite estrelada" is in promotion
    And the "data de início e término da promoção" is registered correctly in the system
    And the promotion is displayed correctly on the promotions page

Scenario: Promotion Registration Failure
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has no promotion
    When the user "Pedro" chooses "cadastrar promoção"
    And the user "Pedro" leaves the "valor promoção" field in blank
    And the user "Pedro" chooses "confirmar promoção"
    Then the user "Pedro" receives an error message of "Por favor, preencha todos os campos obrigatórios"
    And the promoção is not in the system yet
    And the system keeps the hotel "noite estrelada" whitout promotion

Scenario: Automatic Expiration of Promotion
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has an active promotion with "data de término" close
    When a "data de término" of promotion is reached 
    Then the promotion is automatically removed from system
    And the user "Pedro" can see the promotion is expired

Scenario: Successful Promotion Update
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has an existing promotion
    When the user "Pedro" chooses "atualizar promoção"
    And the user "Pedro" modifies the informações da promoção
    And the user "Pedro" chooses "confirmar atualização"
    Then the user "Pedro" receives a message of "Promoção atualizada com sucesso!"
    And the modifications in promotion of hotel "noite estrelada" are reflected in the system
    And the modification of promotion is registered correctly in the system

Scenario: Failed Promotion Update
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has an existing promotion
    When the user "Pedro" chooses "atualizar promoção"
    And the user "Pedro" leaves the promotions informations blank
    And the user "Pedro" chooses "confirmar atualização"
    Then the user "Pedro" receives an error message of "Por favor, preencha todos os campos obrigatórios"
    And the promoção is not updated in the system
    And the previous informations on hotel "noite estrelada" are keeped

Scenario: Successful Promotion Removal
    Given que the user "Pedro" is logged in as "administrador"
    And há uma promoção existente no system for the hotel "noite estrelada"
    When the user "Pedro" accesses the promotions list of hotel
    And the user "Pedro" chooses "remover promoção" in question of the hotel "noite estrelada"
    And the user "Pedro" chooses "confirmar remoção"
    Then the promoção do hotel "noite estrelada" is removed from the system
    And the user "Pedro" receives the message de confirmação "Promoção removida com sucesso"
    And the promoção removida não é mais exibida na página de promoções

Scenario: Cancel Promotion Removal
    Given that the user "Pedro" is logged in as an "administrator"
    And there is an existing promotion in the system for the hotel "noite estrelada"
    When the user "Pedro" accesses the list of promotions for the hotel
    And the user "Pedro" chooses to "remove the promotion" in question from the hotel "noite estrelada"
    And the user "Pedro" chooses the option "cancelar"
    Then the promotion of the hotel "noite estrelada" is not removed from the system
    And the promotion is retained on the promotions page

Scenario: Promotion Value Limits
    Given the user "Pedro" is logged in as "administrador"
    And the hotel "noite estrelada" has no promotion
    When the user "Pedro" chooses "cadastrar promoção"
    And the user "Pedro" fills in the "valor promoção" field with a valor muito alto
    And the user "Pedro" chooses "confirmar promoção"
    Then the user "Pedro" receives an error message of "valor da promoção excede o limite permitido"
