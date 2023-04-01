import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='direct')

messages = {
    'info.debug.notimportant': 'this is not important message',
    'error.warning.important': 'this is an important message',
}

for k, v in messages.items():
    ch.basic_publish(exchange='topic_logs', routing_key=k, body=v)

print('sent')

connection.close()
