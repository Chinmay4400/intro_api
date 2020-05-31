#Messing around with twilio

from twilio.rest import Client

client = Client("AC63386df5b8080869ee943a3b8e9cee74",
                "b1b73a8e65f196f026f62cfde691ca7b"
                )

for msg in client.messages.list():
    print(f"Deleting msg {msg.body}")
    msg.delete()

# msg = client.messages.create(
#         to = "+919826700551",
#         from_ ="+12056712324",
#         body = "Hello from python"
#     )

# print(f"created new msg: {msg.sid}")


