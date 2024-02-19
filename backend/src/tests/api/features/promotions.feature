Feature: Promoções API

    Scenario: Obter uma promoção por ID do quarto
        Given o PromotionService retorna os valores de uma promoção com reservationValue "150.0" e newValue "130.0"
        When uma requisição "GET" é enviada para "promotions/123"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter reservationValue "150.0" e newValue "130.0"

    Scenario: Tentar obter uma promoção inexistente por ID do quarto
        Given não existe uma promoção com ID do quarto "456"
        When uma requisição "GET" é enviada para "promotions/456"
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not found"
        
    Scenario: Obter o valor atual de desconto por ID do quarto
        Given o PromotionService retorna id da promoção "aabb" e valor atual de desconto "20.0"
        When uma requisição "GET" é enviada para "promotions/123/current"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve conter o valor atual de desconto "20.0" e id da promoção "aabb"

    Scenario: Tentar obter o valor atual de desconto para uma promoção inexistente por ID do quarto
        Given não existe uma promoção com ID do quarto "456"
        When uma requisição "GET" é enviada para "promotions/456/current"
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not found"

    Scenario: Registrar uma nova promoção
        Given o PromotionService retorna um documento de promoção user "pedro", adm "True", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "20" e id "65d26a97e24aa3a20694e3aa"
        When uma requisição "POST" é enviada para "promotions/register"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve indicar o sucesso com o documento user "pedro", adm "True", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "20" e id "65d26a97e24aa3a20694e3aa"

    Scenario: Tentar registrar uma nova promoção com discountValue negativo
        Given a solicitação para registrar uma nova promoção é inválida
        When uma requisição "POST" é enviada para "promotions/register" com discountValue negativo
        Then o status da resposta deve ser "422"
        And o JSON da resposta deve conter a mensagem de erro "Promoção não criada"
    
    Scenario: Tentar registrar uma nova promoção com discountValue null
        Given a solicitação para registrar uma nova promoção é inválida
        When uma requisição "POST" é enviada para "promotions/register" com discountValue null
        Then o status da resposta deve ser "422"
        And o JSON da resposta deve conter a mensagem de erro "Input should be a valid number"

    Scenario: Atualizar uma promoção existente
        Given existe uma promoção com ID do quarto "123" 
        And há uma solicitação válida para atualizar essa promoção
        And PromotionService retorna um documento
        When uma requisição "PUT" é enviada para "promotions/update"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve indicar o sucesso com o documento user "pedro", adm "true", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "20" e id "65d26a97e24aa3a20694e3aa"

    Scenario: Tentar atualizar uma promoção inexistente
        Given não existe uma promoção com ID do quarto "456"
        When uma requisição "PUT" é enviada para "promotions/update"
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not found"

    Scenario: Excluir uma promoção
        Given existe uma promoção com ID do quarto "123"
        And há uma solicitação válida para excluir essa promoção
        When uma requisição "DELETE" é enviada para "promotions/delete" com os detalhes da exclusão
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve indicar o sucesso com os elementos id do quarto "123" e o contador "1"

    Scenario: Tentar excluir uma promoção inexistente
        Given não existe uma promoção com ID do quarto "456"
        When uma requisição "DELETE" é enviada para "/delete" com os detalhes da exclusão
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not found"