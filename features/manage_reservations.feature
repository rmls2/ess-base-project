Feature: manage reservations
        As a customer of hotel booking website
        I want to be able to manage my reservations
        then I can delete and change them.

Scenario: edit booking
        Given that the user "Joao" is on the "my reservations" page
        When the user "joão" sees the reservation "Starry Room" and selects the "details" option they are then directed to the "booking details" page which contains a location description
        and displays the fields check-in date filled with "01/05/24", checkout date filled with "05/05/24", number of people filled with "2" and the option "edit reservation"
        When the user "Joao" select the "edit reservation" option
        Then The fields check-in date, checkout date are then displayed on the screen with a "cursor" indicating the possibility of change.
        And just below the option "Save changes"
        When the user "Joao" changes the "number of people" field to "5" and selects the "save changes" option
        Then the system shows a message "change made successfully"
        And the user "joao" is redirected to the "my reservations" page

Scenario: delete reservation
        Given that the user "joao" is on the "my reservations" page
        When the user sees the reservation "Hawaii room" and selects the
        "details" option 
        Then he is directed to the "booking details" page which contains a description of the place and displays the fields check-in date filled with "01/05/24", 
        checkout date filled with "05/05/24", number of people filled with "2" and and the "delete reservation" option
        When the user "joão" selects the "delete reservation" option
        Then the message "are you sure you want to delete this reservation" is displayed with the option below "yes" or "no"
        When the user "joão" selects the "yes" option
        Then the system displays the message "reservation deleted successfully"
        And redirects the user to the "my reservations" page.
