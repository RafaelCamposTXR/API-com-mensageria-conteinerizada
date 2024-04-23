from .rabbitmq import connect, canal, queue_name

# Mensagem a ser enviada
mensagem = 'Mensagem De teste'

# Publica a mensagem na fila
canal.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=mensagem)