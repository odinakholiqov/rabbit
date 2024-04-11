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

# channel.exchange_declare("emails", "direct")
channel.queue_declare(queue="email.notifications")

# channel.queue_bind("email.notification", "emails", "notification")


def send_to_queue(channel, routing_key, email, name, body):
    msg = f"{email}, {name}, {body}"

    channel.basic_publish(
        exchange="",
        routing_key=routing_key,
        body=msg
    )

    print("Message sent to queue")

def main():
    print("* * *")
    sender = input("Sender: ")
    name = input("Name: ")
    body = input("Body: ")

    send_to_queue(channel, "email.notifications", sender, name, body)

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
