import pika

parametros_conexao = pika.ConnectionParameters('localhost')
conexao = pika.BlockingConnection(parametros_conexao)

canal = conexao.channel()
canal.queue_declare(queue='teste')

mensagem = "Mensagem de Teste Enviada"

canal.basic_publish(exchange="",routing_key = 'teste', body=mensagem)

print(f'Mensagem enviada: {mensagem}')
conexao.close()