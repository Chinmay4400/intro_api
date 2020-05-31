#Messing around with twilio

import os
from twilio.rest import Client

client = Client(os.environ['SID'],
                os.environ['auth']
                )

for msg in client.messages.list():
    print(f"Deleting msg {msg.body}")
    msg.delete()

msg = client.messages.create(
        to = "+919826700551",
        from_ ="+12056712324",
        body = "Hello from python"
    )

print(f"created new msg: {msg.sid}")


