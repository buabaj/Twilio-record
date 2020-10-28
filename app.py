#importing the necessary libraries and packages
from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse



app = Flask(__name__)

@app.route("/")
def check_app():
    # returns a simple string to check if the app is working
    return Response("yayy it works!")


#routing the record function to the record page
@app.route("/record", methods=['GET', 'POST'])
def record():   #writing function to record call 
    response = VoiceResponse()   
    response.say('Hello. Your message will be recorded after the beep.') #This message will be said when the call starts
    response.record() #message will be recorded with the record method
    response.hangup() #call will hang up with this method
    return str(response) #the response that was given will be returned


if __name__ == "__main__":
    app.run()
