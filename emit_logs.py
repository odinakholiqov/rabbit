import pika, os, random
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("CLOUDAMQP_URL")

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("Connection is established")

channel.exchange_declare(exchange="logs", exchange_type="fanout")

msg = f"Hello World for the {random.randrange(1,11)}"
channel.basic_publish(exchange="logs", routing_key="", body=msg)
print(f" [x] Sent {msg}")

connection.close()