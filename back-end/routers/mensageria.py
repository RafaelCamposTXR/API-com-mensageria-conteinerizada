import pika, json
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models.schemas import Operation


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

@router.get("/exemplo")
def consumidor():
    def callback(ch, metodos, props, body):
      mensagem = "Banco de Dados entregou a resposta"
      canal.basic_publish(exchange="",routing_key = 'fila1', body=mensagem)
      resposta = json.loads(body)
      if resposta.get('id') == 0:
        print("Requisição Recebida: 0")
      elif resposta.get('id') == 1:
        print("Requisição Recebida: 1")
      conexao.close()

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)

    canal = conexao.channel()
    canal.queue_declare(queue='fila1')

    canal.basic_consume(queue='fila0', auto_ack=True, on_message_callback=callback)

    print("Iniciando processo de consumo")

    canal.start_consuming()