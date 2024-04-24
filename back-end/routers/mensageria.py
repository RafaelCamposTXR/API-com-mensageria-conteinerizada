import pika, json
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models.schemas import Operation
import psycopg2

app = FastAPI()
router = APIRouter()

@router.get("/mensageria")
def consumidor():
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

    nome = Operation(id= 1)
    mensagem = nome.model_dump_json()
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    canal.basic_consume(queue='fila1', auto_ack=True, on_message_callback=callback)
    print("Aguardando Resposta do Banco de Dados")
    canal.start_consuming()

    
    return app.state.mensagem

@router.get("/filaBanco")
def consumidor():
    def callback(ch, metodos, props, body):
      
      resposta = json.loads(body)
      if resposta.get('id') == 4:
        print("Requisição Recebida: Retornar Aeroportos")

      elif resposta.get('id') == 5:
        print("Requisição Recebida: Retornar Aeroportos Por Origem")

      elif resposta.get('id') == 6:
        print("Requisição Recebida: Retornar vôos para a Data Informada")

      elif resposta.get('id') == 7:
        print("Requisição Recebida: Retornar voos com a menor tarifa para um dado número de passageiros")
      
      elif resposta.get('id') == 8:
        print("Requisição Recebida: Efetua compra e reserva dos vôos e tarifas selecionados e retorna o localizador")
        
      mensagem = "Crud acontece aqui"
      canal.basic_publish(exchange="",routing_key = 'fila1', body=mensagem)
      conexao.close()

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)

    canal = conexao.channel()
    canal.queue_declare(queue='fila1')

    canal.basic_consume(queue='fila0', auto_ack=True, on_message_callback=callback)

    print("Iniciando processo de consumo")

    canal.start_consuming()