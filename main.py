from twilio.rest import Client
from msg import (msg)

account_sid = 'ACd673c80d33de9debb49a6342f5084463'
auth_token = 'a1fbb4c6b7e2cf838e631fd80c633d33'

client = Client(account_sid, auth_token)

client.messages.create(
    to="+14637012190",
    from_="+18479093707",
    body=msg,
)
