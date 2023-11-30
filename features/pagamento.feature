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

Scenario: Disparo de Email com Comprovante de Pedido
Given que o usuário "Alice" realizou uma transação com sucesso
And o sistema possui o endereço de email válido do usuário "Alice"
When o sistema dispara um email para o usuário "Alice" com o comprovante de pedido
Then o usuário "Alice" deve receber um email contendo o comprovante de pedido como anexo
And o sistema deve registrar o envio do email no histórico de comunicações

Scenario: Remoção de Promoção com sucesso
Given que o usuário "Pedro" está logado como "administrador"
And há uma promoção existente no sistema para o hotel "noite estrelada"
When o usuário "Pedro" acessa a lista de promoções do hotel
And o usuário "Pedro" escolhe remover a promoção em questão do hotel "noite estrelada"
Then a promoção do hotel "noite estrelada" é removida do sistema
And o usuário "Pedro" recebe uma mensagem de confirmação "Promoção removida com sucesso"