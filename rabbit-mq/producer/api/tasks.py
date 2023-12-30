from celery import shared_task
import pika

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)

@shared_task
def send_message(message):

    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        connection.close()
        return 'Message sent successfully'
    except Exception as e:
        print(e)
        return 'Message not sent'
    
# write a function to know whats on queue
@shared_task
def get_queue():
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        queue = channel.queue_declare(queue='hello')
        return queue.method.message_count
    except Exception as e:
        print(e)
        return 'Queue not found'
