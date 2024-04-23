import pika

# Configurações de conexão com o RabbitMQ
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'guest'
RABBITMQ_PASSWORD = 'guest'

# Inicialização da conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    port=RABBITMQ_PORT,
    credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
))
channel = connection.channel()

# Declaração de uma fila (opcional)
channel.queue_declare(queue='minha_fila')