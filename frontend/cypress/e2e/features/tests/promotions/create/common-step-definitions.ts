import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

Given("o usuário está na página {string}", (page: string) => {
    cy.visit(page);
});

Given("o usuário está na página {string}", (page: string) => {
    cy.visit(page);
});

When("o usuário clica em {string}", (button: string) => {
    cy.getDataCy(button).click();
});

When('o usuario clica em "confirmar"', () => {
    cy.getDataCy('Confirmar').click();
}
);
Then("o usuário volta para a página "quartos" e vizualiza valor anterior "{string}" e valor atual "{string}"", (numOld: text, numNew: text) => {
    cy.getDataCy('oldPrice').should('contain', numOld);
    cy.getDataCy('r147Diria').should('contain', numNew);
});