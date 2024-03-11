Feature: Criar Promoção
As a usuário admin
I want to criar uma nova Promoção
so that eu possa usar meu sistema

Scenario: Criar uma Promoção com sucesso
Given o usuário está na página "quartos"
When o usuário clica em "Cadastrar promoção"
When o usuário preenche o campo "Valor" com "20"
And o usuário clica em "Confirmar"
Then o usuário volta para a página "quartos" e vizualiza valor anterior "100" e valor atual "80"