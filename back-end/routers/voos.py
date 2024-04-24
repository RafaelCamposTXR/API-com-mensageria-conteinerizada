from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from models1.schemas import VoosSchema, Operation
import pika

app = FastAPI()
router = APIRouter()

#
# RETORNAR VOOS
#

@router.post("/voos")
async def retornar_voos(date: str):
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

    nome = Operation(id= 6, data= date)
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

@router.post("/voos/search")
async def pesquisar_voos(passengers: int):
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

  nome = Operation(id= 7, passageiros = passengers)
  mensagem = nome.model_dump_json()
  canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
  print(f'Mensagem enviada: {mensagem}')

  canal.basic_consume(queue='fila1', auto_ack=True, on_message_callback=callback)
  print("Aguardando Resposta do Banco de Dados")
  canal.start_consuming()

  return app.state.mensagem

#
# EFETUAR COMPRA
#

@router.post("/voos/purchase/{id}")
async def efetuar_compra(id_voo: int, passengers: int, preco: float):

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

  nome = Operation(id= 8, id_voo= id_voo, passageiros = passengers, preco = preco)
  mensagem = nome.model_dump_json()
  canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
  print(f'Mensagem enviada: {mensagem}')

  canal.basic_consume(queue='fila1', auto_ack=True, on_message_callback=callback)
  print("Aguardando Resposta do Banco de Dados")
  canal.start_consuming()

  return app.state.mensagem
