"""
Producer

"""
import pika, os, sys
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("CLOUDAMQP_URL")

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("Connection is established")

channel.queue_declare(queue="hello")

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(f" [x] Sent {message}")