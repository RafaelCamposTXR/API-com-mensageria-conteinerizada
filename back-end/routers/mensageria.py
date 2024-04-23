import pika
from fastapi import FastAPI, APIRouter, Depends, HTTPException

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


    mensagem = "Requisicao feita pelo usuário vai aqui"
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
      print(f"Requisição Recebida: {body}")

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)

    canal = conexao.channel()
    canal.queue_declare(queue='fila1')

    canal.basic_consume(queue='fila0', auto_ack=True, on_message_callback=callback)

    print("Iniciando processo de consumo")

    canal.start_consuming()