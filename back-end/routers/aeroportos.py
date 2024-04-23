from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models import crud


app = FastAPI()
router = APIRouter()


#
# RETORNAR AEROPORTOS
#

@router.get("/aeroportos", response_model=List[AeroportosSchema])
def retornar_aeroportos():
    
    aeroportos = crud.get_aeroportos()
    return aeroportos

#
# RETORNAR AEROPORTOS POR ORIGEM
#

@router.get("/aeroportos/{origem}/destinos", response_model=List[AeroportosSchema])
def retornar_aeroportos_por_origem(origem: str, db: Session = Depends(obter_db)):
    
    mensagem = "id: 4"

    aeroportos_destino = db.query(Aeroportos).filter(Aeroportos.cidade == origem).all()
    return aeroportos_destino

#
# CRUD
#

# create
@router.post("/aeroportos/", response_model=AeroportosSchema)
def criar_aeroporto(aeroporto: AeroportosSchema, db: Session = Depends(obter_db)):

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)
    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    mensagem = "Requisicao feita pelo usuário vai aqui"
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    db_aeroporto = Aeroportos(**aeroporto.dict())
    db.add(db_aeroporto)
    db.commit()
    db.refresh(db_aeroporto)
    return db_aeroporto

# get
@router.get("/aeroportos/{aeroporto_id}", response_model=AeroportosSchema)
def obter_aeroporto(aeroporto_id: int, db: Session = Depends(obter_db)):

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)
    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    mensagem = "Requisicao feita pelo usuário vai aqui"
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    db_aeroporto = db.query(Aeroportos).filter(Aeroportos.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    return db_aeroporto

# update
@router.put("/aeroportos/{aeroporto_id}", response_model=AeroportosSchema)
def atualizar_aeroporto(aeroporto_id: int, aeroporto: AeroportosSchema, db: Session = Depends(obter_db)):

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)
    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    mensagem = "Requisicao feita pelo usuário vai aqui"
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    db_aeroporto = db.query(Aeroportos).filter(Aeroportos.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    for campo, valor in vars(aeroporto).items():
        setattr(db_aeroporto, campo, valor)
    db.commit()
    db.refresh(db_aeroporto)
    return db_aeroporto

# delete
@router.delete("/aeroportos/{aeroporto_id}")
def deletar_aeroporto(aeroporto_id: int, db: Session = Depends(obter_db)):

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)
    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    mensagem = "Requisicao feita pelo usuário vai aqui"
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')
    
    db_aeroporto = db.query(Aeroportos).filter(Aeroportos.id == aeroporto_id).first()
    if db_aeroporto is None:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado")
    db.delete(db_aeroporto)
    db.commit()
    return {"message": "Aeroporto deletado com sucesso"}