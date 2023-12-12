Feature: atração
As a Usuario do sistema
I want to visualizar informações detalhadas sobre uma atração
so that Eu possa avaliar se vale a pena reservar o atraçao

Scenario: visualizar todas as fotos
Given eu estou na página de "atração"
And eu posso ver 2 fotos sobre a atração
When eu seleciono "mais fotos"
Then eu ainda estou na pagina de "atração"
And eu posso ver 5 fotos sobre a "atração"

Scenario: Ver todas as avaliações
Given eu estou na página de "atração"
And eu posso ver 3 avaliações com as notas "8.63", “8,63 e "9"
When eu seleciono "ver todas as avaliações"
Then eu ainda estou na página de "atração"
And eu posso ver 5 avaliações com as notas "8.63", ”8,63”, "9", 6.67" e "8"

Scenario: Selecionar atração relacionada
Given eu estou na página de "atração"
And eu posso ver o nome "As Coloridas" e o CEP "55870000"
When eu seleciono a atração "Aconchego Familiar-Piscina Privativa" em "atrações semelhantes"
Then eu sou redirecionado para a pagina de "atração"
And posso ver o nome "Aconchego Familiar-Piscina Privativa" e o CEP "55870000"

Scenario: Realizar reservar
Given eu estou na página de "atração"
And eu posso ver a atração "As Coloridas" com o valor da atração "R$500.00"
When eu seleciono “Realizar uma reserva”
Then eu sou redirecionado para a página de "pagamentos"
And eu posso ver o nome da atração "As Coloridas" com o valor "R$500.00" em "Valor a pagar"

