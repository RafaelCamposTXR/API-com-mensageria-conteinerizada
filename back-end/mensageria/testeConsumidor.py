import pika

def callback(ch, metodos, props, body):
  print(f"Mensagem Recebida: {body}")

parametros_conexao = pika.ConnectionParameters('localhost')
conexao = pika.BlockingConnection(parametros_conexao)

canal = conexao.channel()
canal.queue_declare(queue='teste')

canal.basic_consume(queue='teste', auto_ack=True, on_message_callback=callback)

print("Iniciando processo de consumo")

canal.start_consuming()