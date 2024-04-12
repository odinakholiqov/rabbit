import pika, os, sys, random, time
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("CLOUDAMQP_URL")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def main(num):
    message = f"{num}: Hello World!"

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))

    print(f" [x] Sent {message}")

while True:
    try:
        main(random.randrange(1, 5))
        time.sleep(2)
    except KeyboardInterrupt as e:
        connection.close()
        print("Bye")
