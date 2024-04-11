"""
Consumer
"""

import pika, os, sys
from dotenv import load_dotenv

load_dotenv()
url = os.environ.get("CLOUDAMQP_URL")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

print("Connection is established")

channel.queue_declare(queue='hello')

def main():
    def callback(channel, method, properties, body):
        print(f"Message received: {body}")

    channel.basic_consume(queue="email.notifications", auto_ack=True, on_message_callback=callback)

    print("Waiting for new msg")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

