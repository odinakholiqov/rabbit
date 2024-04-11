"""
Producer

"""
import pika, os
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("CLOUDAMQP_URL")

print(url)
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

send_to_queue(channel, "email.notifications", "odina@admin.com", "Odina", "Here if your job offer!")
send_to_queue(channel, "email.notifications", "odina@admin.com", "Odina", "Your salary is $3000")
send_to_queue(channel, "email.notifications", "odina@admin.com", "Odina", "Congratulations!")

try:
    connection.close()
    print("Connection is closed")
except Exception as e:
    print(f"Error {e}")

