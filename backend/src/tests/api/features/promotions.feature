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

    Scenario: Registrar uma nova promoção
        Given o PromotionService retorna um documento de promoção user "pedro", adm_key "6789", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "20" e id "65d26a97e24aa3a20694e3aa"
        When uma requisição "POST" é enviada para "promotions/register"
        Then o status da resposta deve ser "201"
        And o JSON da resposta deve indicar o sucesso com o documento user "pedro", adm_key "6789", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "20" e id "65d26a97e24aa3a20694e3aa"

    Scenario: Tentar registrar uma nova promoção com discountValue negativo
        Given a solicitação para registrar uma nova promoção é inválida com o request: user "pedro", adm_key "6789", hotel "noite estrelada", room_id "womrjatajDEa1X0as0W7lVVb", reservationValue "150", discountValue "-20"
        When uma requisição "POST" é enviada para "promotions/register" 
        Then o status da resposta deve ser "422"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not created"
    
    Scenario: Atualizar uma promoção existente
        Given existe uma promoção com ID do quarto "123" e a requisição tem user "pedro", adm_key "6789", currentDiscountValue "25.0", newDiscountValue  "20.0" 
        When uma requisição "PUT" é enviada para "promotions/update"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve indicar o sucesso com o documento user "pedro", adm_key "6789", hotel "noite estrelada", room_id "123", reservationValue "150.0", discountValue "20.0" e id "65d26a97e24aa3a20694e3aa"

    Scenario: Tentar atualizar uma promoção inexistente
        Given não existe uma promoção com ID do quarto "456" e a requisição tem user "pedro", adm_key "6789", currentDiscountValue "25.0", newDiscountValue  "20.0"
        When uma requisição "PUT" é enviada para "promotions/update"
        Then o status da resposta deve ser "404"
        And o JSON da resposta deve conter a mensagem de erro "Promotion not found"

    Scenario: Excluir uma promoção
        Given existe uma promoção com ID do quarto "123" e chave de administrador "6789"
        When uma requisição "DELETE" é enviada para "promotions/delete/6789/123"
        Then o status da resposta deve ser "200"
        And o JSON da resposta deve indicar o sucesso com os elementos id do quarto "123" e o contador "1"

    Scenario: Usuario não autorizado a Excluir promoção
        Given existe uma promoção com ID do quarto "123" e chave de administrador "678"
        When uma requisição "DELETE" é enviada para "promotions/delete/6789/123"
        Then o status da resposta deve ser "401"