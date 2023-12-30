import pika, sys, os, time

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)

def consume():
    def callback(ch, method, properties, body):
        time.sleep(5)
        print(" [x] Received %r" % body)

    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except Exception as e:
        print(e)
        return 'Queue not found'

if __name__ == '__main__':
    try:
        consume()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)        