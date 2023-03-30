import pika

# making the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# making the channel
ch1 = connection.channel()

# making queue or checking if exists
ch1.queue_declare(queue='hello')

# sending a message
ch1.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# making sure it is sent
print('Message sent.')

connection.close()
