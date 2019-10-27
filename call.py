from twilio.rest import Client
import urllib.parse, sys

phonenumber = sys.argv[1]
alertcontext = sys.argv[2]

twiliohtml = "https://handler.twilio.com/twiml/EH99809d3ed340a0ebd3a5323d5074b9c4?Alert="
alerturl = urllib.parse.quote(alertcontext)
twiliohtml+= alerturl
print(phonenumber)
print(twiliohtml)

#account_sid = 'AC5fe8b65b16dee6ee502caeabb14f626b'
#auth_token = 'bd06dc8983242b63951c439f6ff8e9fe'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url=twiliohtml,
                        to=phonenumber,
                        from_='+972587992444'
                    )
#output
print(call.sid)
