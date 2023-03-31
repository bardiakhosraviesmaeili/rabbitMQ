import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='first', durable=True)

message = 'This is the message from the sender.'

ch.basic_publish(exchange='', routing_key='first', body=message,
                 properties=pika.BasicProperties(delivery_mode=2, headers={'name': 'bardia'}))

print('send message')

connection.close()
