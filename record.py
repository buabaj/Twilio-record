#import necessary library and modules.
from twilio.rest import Client

#assign your account credentials to the corresponding variables.
account_sid = 'your account sid goes here'
auth_token = 'your auth token goes here'

#passing in the required args to the Client module
client = Client(account_sid, auth_token)

#intantiate call and pass in necessary parameters to method
call = client.calls.create(
                        record=True, #records call
                        status_callback='http://recordingURL.io/', #URL that Twilio will send recording to
                        url='http://demo.twilio.com/docs/voice.xml', #URL that Twilio will fetch special XML doc
                        to='+15017122661', #number you want to call
                        from_='+13238591607' #your Twilio number
                    )

print(call.sid) #print unique SID number that identifies call