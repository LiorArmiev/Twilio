#load module
from twilio.rest import Client
import urllib.parse, sys

phonenumber = sys.argv[1]
alertcontext = sys.argv[2]

twiliohtml = "https://handler.twilio.com/twiml/xxxx?Alert="
alerturl = urllib.parse.quote(alertcontext)
twiliohtml+= alerturl
print(phonenumber)
print(twiliohtml)

#account_sid = ''
#auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url=twiliohtml,
                        to=phonenumber,
                        from_='+972587992444'
                    )
#output
print(call.sid)

#test feature