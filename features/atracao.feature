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
And eu posso ver 3 avaliações com as notas "8.63" e "9"
When eu seleciono "ver todas as avaliações"
Then eu ainda estou na página de "atração"
And eu posso ver 5 avaliações com as notas "8.67", "9", 6.67", "8" e "9.1"