import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

//Scenario criar uma Promoção com sucesso
//Given: common-step-definitions.ts

When('o usuário preenche o campo "{string}" com "{string}"', (field: string, value: string) => {
    cy.getDataCy(field).type(value);
    cy.getDataCy(button).click();
});

Then('o usuário volta para a página "quartos" e vizualiza valor anterior "{string}" e valor atual "{string}"', 
    (oldValue: string, newValue: string)) => {
        cy.getDataCy(oldValue).should("contain", "100");
        cy.getDataCy(newValue).should("contain", "80");
    }