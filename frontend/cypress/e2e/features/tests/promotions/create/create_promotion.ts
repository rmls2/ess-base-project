import { Given, Then, When } from "@badeball/cypress-cucumber-preprocessor";

//Scenario criar uma Promoção com sucesso
//Given: common-step-definitions.ts

When('o usuário preenche o campo "{string}" com "{string}"', (field: string, value: string) => {
    cy.getDataCy(field).type(value);
    cy.getDataCy(button).click();
});