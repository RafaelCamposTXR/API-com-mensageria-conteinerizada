import pika, json
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models1.schemas import Operation
from models1 import crud
import psycopg2

app = FastAPI()
router = APIRouter()

@router.get("/teste-mensageria")
def produtor():
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

    nome = Operation(id= -1)
    mensagem = nome.model_dump_json()
    canal.basic_publish(exchange="",routing_key = 'fila0', body=mensagem)
    print(f'Mensagem enviada: {mensagem}')

    canal.basic_consume(queue='fila1', auto_ack=True, on_message_callback=callback)
    print("Aguardando Resposta do Banco de Dados")
    canal.start_consuming()

    
    return app.state.mensagem

@router.get("/BD_Consumidor")
def consumidor_requisicoes():
    def callback(ch, metodos, props, body):
      resposta = json.loads(body)
      if resposta.get('id') == 4:
        print(f"Requisição Recebida:{json.dumps(crud.get_voos())} ")
        mensagem = json.dumps(crud.get_voos())

      elif resposta.get('id') == 5:
        print("Requisição Recebida: Retornar Aeroportos Por Origem")
        mensagem = json.dumps(crud.get_aeroportos_por_origem(resposta.get('origem')))
        print(mensagem)

      elif resposta.get('id') == 6:
        print("Requisição Recebida: Retornar vôos para a Data Informada")
        mensagem = json.dumps(crud.get_voo_por_data(resposta.get('data')))
        print(mensagem)

      elif resposta.get('id') == 7:
        print("Requisição Recebida: Retornar voos com a menor tarifa para um dado número de passageiros")
        mensagem = json.dumps((crud.get_voos_menor_tarifa(resposta.get('passageiros'))))
        print(mensagem)
        
      elif resposta.get('id') == 8:
        print("Requisição Recebida: Efetua compra e reserva dos vôos e tarifas selecionados e retorna o localizador")
        mensagem = json.dumps(crud.get_voo_por_data(resposta.get('id_voo', 'passageiros', 'preco')))
        print(mensagem)

      elif resposta.get('id') == -1:
        mensagem = "Mensagem de teste recebida com sucesso"

      else:
        mensagem = "Erro de Mensageria"
      canal.basic_publish(exchange="",routing_key = 'fila1', body=mensagem)

    parametros_conexao = pika.ConnectionParameters('localhost')
    conexao = pika.BlockingConnection(parametros_conexao)

    canal = conexao.channel()
    canal.queue_declare(queue='fila1')

    canal.basic_consume(queue='fila0', auto_ack=True, on_message_callback=callback)

    print("Iniciando processo de consumo")

    canal.start_consuming()