import pika

# Configurações de conexão com o RabbitMQ
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'

# Inicialização da conexão com o RabbitMQ
connect = pika.BlockingConnection(pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    port=RABBITMQ_PORT,
    credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
))
canal = connect.channel()

# Declaração de uma fila (opcional)
canal.queue_declare(queue='fila')

queue_name = 'fila'

def callback(ch, method, properties, body):
    print("Mensagem recebida:", body.decode())