Scenario: User successfully completes the order
    Given the user "João" is the confirmation page of hotel "noite estrelada"
    And the user "João" complete the purchase of "noite estrelada"
    When the system process the reservation de the user "João" of hotel "noite estrelada"
    Then the system sends a email of confirmation of reservation of the user "João" with the receipt of "noite estrelada"
    And the user "João" can see the receipt of "noite estrelada"

//TODO completes trigger email scenarios