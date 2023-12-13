Feature: Registration and login
        As a user of reservation services
        I want to register on the platform
        So that I can make reservations

Scenario: user registration not yet registered
        Given that I am an email user "joao@gmail.com" not registered on the platform
        When I access the "register" page and fill in all the "name", "email", "password" and "phone" fields 
        with "João Lendo", "joao@gmail.com", "imagine-all-the-people", "2345678", respectively
        And select the "register" option
        Then I get a confirmation message "thank you for registering your account".
        And I am automatically redirected to the "home" page, now authenticated as a registered user

Scenario: failure to register
        Given that I am an email user "joao@gmail.com" I am on the "home" page and I am not registered on the platform
        When I access the "register" page and I fill in the email field with "joao@gmail.com" and I leave the phone field "blank"
        And click on the "Register" button
        Then I receive an error message "fill in all registration fields" indicating that all required fields must be filled in
        And unfilled fields are highlighted for correction

Scenario: logging into the system successfully
        Given I am a user of the email "joao@gmail.com" registered already on the platform and I am on the "login" page
        When I fill in the email field with "joao@gmail.com" and fill in the password field with "2345678" and select the "login" option
        Then I am redirected to the "home" page, now authenticated as a user.

Scenario: failed to log into the system
        Given I am an email user "joao@gmail.com"already logged in to the platform and I am on the "login" page
        When I try to log in by filling in the "email field" with the email "lendo@gmail.com"
        And choose the option "Enter"
        Then I get a message "incorrect email or password!" indicating that the credentials are incorrect
        And I am instructed to fill in the "email field" and "password field.

Scenario: recovering forgotten password
        Given I am an email user "joao@gmail.com" already logged in to the platform and I am on the "login" page
        When I select the "forgot password?"
        Then I receive the message "we have sent the recovery email to your registered email"
        And I am redirected to the "login" page and I can notice that the "email" field and the "password" field are not filled in.
