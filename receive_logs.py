import pika, os, random
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("CLOUDAMQP_URL")

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("Connection is established")

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

print('[*] Waiting for logs. To exit press CTRL+C')


def callback(ch, meethod, properties, body):
    print(f"[x] {body}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()