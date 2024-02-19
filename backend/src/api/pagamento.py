from fastapi import APIRouter, HTTPException
from src.schemas.pagamento import Cartao, getDB, saveDB

router = APIRouter()

@router.post("/post_payment/", status_code=201, tags=['pagamento'],response_model=Cartao)
async def add_card(cartao:Cartao):
    db = getDB()
    if cartao.dict() in db['cartoes']:
        raise HTTPException(status_code=422, detail="já existe este cartão")
    db['cartoes'].append(cartao.dict())
    saveDB(db)
    return cartao

@router.get('/get_payment/', status_code=200, tags=['pagamento'], response_model=list[Cartao])
async def list_card(cpf:str):
    parametro = cpf
    if parametro == None:
        raise HTTPException(status_code=204, detail="não há conteudo na pesquisa")
    
    lista_c = []
    for i in getDB()['cartoes']:
        if parametro == i['cpf']:
            lista_c.append(i)
    
    return lista_c

@router.put('/update_payment/', status_code=200, tags=['pagamento'], response_model=Cartao)
async def update_card(cpf:str,cartao:str, novo_cartao:Cartao):
    db = getDB()
    cont = 0
    for i in db['cartoes']:
        if cpf == i['cpf'] and cartao == i['numero_c']:
            db['cartoes'][cont] = novo_cartao.dict()
            saveDB(db)
            return novo_cartao
        cont += 1    
    raise HTTPException(status_code=204, detail="não há conteudo na pesquisa")

@router.delete('/delete_payment/', status_code=200, tags=['pagamento'], response_model=str)
async def update_card(cpf:str,cartao:str):
    db = getDB()
    cont = 0
    for i in db['cartoes']:
        if cpf == i['cpf'] and cartao == i['numero_c']:
            del db['cartoes'][cont]
            saveDB(db)
            return "cartão excluido"
        cont += 1    
    raise HTTPException(status_code=204, detail="não há conteudo na pesquisa")