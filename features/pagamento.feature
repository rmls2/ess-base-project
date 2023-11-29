Feature: Pagamento
    As a administrador responsável pelo sistema de pagamento
    I want gerenciar métodos de pagamento e promoções
    So that eu possa facilitar transações e fornecer benefícios aos usuários


Scenario: Cadastro de Promoção com sucesso
Given o usuário "Pedro" está logado como "administrador"
And o hotel "noite estrelada" está sem promoção
When o usuário "Pedro" escolher "cadastrar promoção"
And o usuário "Pedro" preenche o campo "valor promoção"
And o usuário "Pedro" escolhe "confirmar promoção"
Then o usuário "Pedro" recebe mensagem de "Promoção cadastrada com sucesso!"
And o hotel "noite estrelada" está em promoção

Scenario: Cadastro de Promoção com falha
Given o usuário "Pedro" está logado como "administrador"
And o hotel "noite estrelada" está sem promoção
When o usuário "Pedro" escolher "cadastrar promoção"
And o usuário "Pedro" deixa o campo "valor promoção" em branco
And o usuário "Pedro" escolhe "confirmar promoção"
Then o o usuário "Pedro" recebe mensagem de erro "Por favor, preencha todos os campos obrigatórios"

Scenario: Atualização de Promoção com sucesso
Given o usuário "Pedro" está logado como "administrador"
And o hotel "noite estrelada" possui uma promoção existente
When o usuário "Pedro" escolhe "atualizar promoção"
And o usuário "Pedro" modifica as informações da promoção
And o usuário "Pedro" escolhe "confirmar atualização"
Then o usuário "Pedro" recebe mensagem de "Promoção atualizada com sucesso!"
And as alterações na promoção do hotel "noite estrelada" são refletidas no sistema

Scenario: Atualização de Promoção com sucesso
Given o usuário "Pedro" está logado como "administrador"
And o hotel "noite estrelada" possui uma promoção existente
When o usuário "Pedro" escolhe "atualizar promoção"
And o usuário "Pedro" deixa as informações da promoção em branco
And o usuário "Pedro" escolhe "confirmar atualização"
Then o usuário "Pedro" recebe mensagem de erro "Por favor, preencha todos os campos obrigatórios"