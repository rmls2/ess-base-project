Feature: Página de cadastro e login.
    As a user of reservation services
    I want to register on the platform
    So that I can make reservations

scenario: user registration not yet registered
    Given that I am an email user "joao@gmail.com" not registered on the platform
    When I access the "register" page and fill in all the "name", "email", "password" and "phone" fields 
    with "João Lendo", "joao@gmail.com",
    "imagine-all-the-people", "2345678", respectively
    And click on the "Register" button
    Then I get a confirmation message "thank you for registering your account".
    And I am automatically redirected to the "home" page, now authenticated as a registered user

scenario: failure to register
    Given that I am an email user "joao@gmail.com" I am on the "home" page and I am not registered on the platform
    When I access the "register" page and I try to proceed without filling in the "phone" field
    And click on the "Register" button
    Then I receive an error message indicating that all required fields must be filled in
    And unfilled fields are highlighted for correction

scenario: logging into the system successfully
    Since I am a user of the email "joao@gmail.com" registered on the platform and I am on the "login" page
    When I correctly fill in the "email" and "password" fields
    And choose the option "Enter"
    Then I am redirected to the "home" page, now authenticated as a user.

scenario: failed to log into the system
    Since I am an email user "joao@gmail.com"already logged in to the platform and I am on the "login" page
    When I try to log in by filling in the "email field" with the email "lendo@gmail.com"
    And choose the option "Enter"
    Then I get a message "incorrect email or password!" indicating that the credentials are incorrect
    And I am instructed to fill in the "email field" and "password field.

scenario: recovering forgotten password
    Since I am an email user "joao@gmail.com" already logged in to the platform and I am on the "login" page
    When I select the "forgot password?"
    Then I receive the message "we have sent the recovery email to your registered email"
    And I am redirected to the "login" page and I can notice that the "email" field and the "password" field are not filled in.
