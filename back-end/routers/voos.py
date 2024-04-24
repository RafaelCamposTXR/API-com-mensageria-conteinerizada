from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models.schemas import VoosSchema, AeroportosSchema, ComprasSchema, UsuariosSchema, Operation
import pika

app = FastAPI()
router = APIRouter()

# conectar com o banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#
# RETORNAR VOOS
#

@router.get("/voos/{date}", response_model=list[VoosSchema])
async def retornar_voos(date: str, db: Session = Depends(obter_db)):

    app.state.mensagem = ""
    def callback(ch, metodos, props, body):
      print(f"Mensagem Recebida: {body}")
      conexao.close()
      app.state.mensagem = body
      return 
    
    

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)

    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    nome = Operation(id= 1, )
    mensagem = nome.model_dump_json()
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    canal.basic_consume(queue='fila1', auto_ack=True, on_message_callback=callback)
    print("Aguardando Resposta do Banco de Dados")
    canal.start_consuming()

    
    return app.state.mensagem

#
# PESQUISAR VOOS
#

@router.get("/voos/search", response_model=List[VoosSchema])
async def pesquisar_voos(origin: int, destination: int, date: str, passengers: int, db: Session = Depends(obter_db)):
  return

#
# EFETUAR COMPRA
#

@router.post("/voos/purchase/{id}", response_model=dict)
async def efetuar_compra(id: str, passengers: int, db: Session = Depends(obter_db)):

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)
    canal = conexao.channel()
    canal.queue_declare(queue='fila0')
    canal.queue_declare(queue='fila1')

    mensagem = "Requisicao feita pelo usuário vai aqui"
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')
    
    voo = db.query(Voos).filter(Voos.id == id).first()
    if not voo:
        raise HTTPException(status_code=404, detail="Voo não encontrado")
    total_price = voo.preco * passengers
    return {"message": "Compra realizada com sucesso", "localizador_reserva": "XYZ123", "numero_etickets": passengers}

