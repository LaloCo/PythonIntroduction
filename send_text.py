from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC03a3fac9c225f629f97bb3abe08f34e5"
# Your Auth Token from twilio.com/console
auth_token  = "6208485a54865a2bffccd2eb00684458"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+527711686391", 
    from_="+19492734551",
    body="I want to know what interesting thing could I do with this!")

print("SMS ", message.sid, " sent.")