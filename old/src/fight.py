from flask import Flask, request
from twilio.rest import TwilioRestClient
from twilio import twiml
import ml

"""
To Do: pull tags better  let voice go through  let user change receiver's phone number? Add
web front end? do ml
"""

# App variables
app = Flask(__name__)
app.config.from_pyfile('environment.cfg')
model = 1 #make model to be trained with texts
my_number = "+18587294421" #set to my phone number
other_number = False #set to other's phone number
default_client = 'jenny'


# Instantiate twilio client
client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])

"""
Let the user
1) Buy a Twilio number
2) configure that number to hit the endpoints of my app

or have 1 twilio number, owned by me.
"""
# create new message instance
@app.route("/sms", methods=['GET','POST'])
def sms():
    # find user using the number that sent the incoming text

    # validate that message came from valid number
    # make new message instance
    send_to = other_number if (this_message.From == @user.my_number) else @user.my_number

    message = client.messages.create(
        body= this_message.body,
        to= send_to,
        from_="+18582155230"
    )

# Forwards call to other person
@app.route("/forward", methods=['GET','POST'])
def forward():
    from_number = request.values.get('PhoneNumber',None)
    send_to = other_number if (from_number == my_number) else my_number

    resp = twiml.Response()
    with resp.dial() as r:
        r.number(send_to)

    return str(resp)

@app.route("/tag", methods=['POST']")
def tag():
    pass

if __name__ == "__main__":
    app.run()
