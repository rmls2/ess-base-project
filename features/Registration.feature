Feature: Cadastrar usuário na plataforma de booking

As a user of reservation services
I want to register on the platform
So that I can make reservations

Scenario: User Registration on the Booking Platform

Given that I am a user of the reservation services and I am on the "registration page"

when I correctly fill in the fields "Name", "surname", "email", "password", "telephone"

And click on the "Register" button

Then I received a confirmation message stating that the registration was successful.


Scenario: Unsuccessful Registration Attempt on the Booking Platform

Since I am on the "registration page"

And I try to proceed without filling in all the required fields, leaving at least one of them blank

when I click on the "Register" button

Then I receive an error message indicating that all required fields must be filled in
And unfilled fields are highlighted for correction