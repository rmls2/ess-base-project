Scenario: User successfully completes the reservation
    Given the user "João" has successfully completed the purchase of "noite estrelada"
    When the system processes the reservation for the user "João" at the hotel "noite estrelada"
    Then the system sends an email of confirmation to the user "João"
    And the email contains the method of "payment", "product" "purchased", "total" "amount", and "user's name"
    And the user "João" can view the reservation receipt for "noite estrelada" in the email

//TODO completes trigger email scenarios