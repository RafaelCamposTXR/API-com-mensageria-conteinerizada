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
    canal.queue_declare(queue='teste')


    canal.basic_consume(queue='teste', auto_ack=True, on_message_callback=callback)
    print("Iniciando processo de consumo")

    canal.start_consuming()
    return app.state.mensagem