from pydantic import BaseModel
import json

def getDB():
    with open('src/db/db.json', 'r') as dbj:
        db = json.load(dbj)
    return db

def saveDB(db):
    with open('src/db/db.json', 'w') as dbj:
        json.dump(db, fp=dbj, indent=4)

class Cartao(BaseModel):
    cpf: str 
    nome_c: str 
    numero_c : str
    data_c: str
    cvv: str
    tipo_c: bool #True -> credito, False -> debito 

class Procura(BaseModel):
    cpf: str
    
if __name__ == '__main__':
    c_1 = Cartao(cpf="00000000000", nome_c="cartao_1",numero_c="1234123412341234",data_c= "1034", cvv="123", tipo_c=True)
    c_2 = Cartao(cpf="10000000000", nome_c="cartao_1",numero_c="2234123412341234",data_c= "1134", cvv="200", tipo_c=False)
    c_3 = Cartao(cpf="20000000000", nome_c="cartao_1",numero_c="3234123412341234",data_c= "1234", cvv="300", tipo_c=True)

    db = getDB()
    db['cartoes'].append(c_1.dict())
    db['cartoes'].append(c_2.dict())
    db['cartoes'].append(c_3.dict())
    saveDB(db)