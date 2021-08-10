from twilio.rest import Client
from msg import (msg)

account_sid = 'ACd673c80d33-------'
auth_token = 'a1fbb4c6b7e2c-------'

client = Client(account_sid, auth_token)

client.messages.create(
    to="+14637012190",
    from_="+18479093707",
    body=msg,
)
