import pika

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