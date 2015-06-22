from flask import Flask, request
from twilio.rest import TwilioRestClient
from twilio import twiml

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
stopwords = [line.strip() for line in open('stopwords.txt')]

# Instantiate twilio client
client = TwilioRestClient(app.config['ACCOUNT_SID']  app.config['AUTH_TOKEN'])

@app.route("/sms"  methods=['GET' 'POST'])
def sms():
    this_message = client.messages.list()[-1]
    if is_tag(message):
        last_message = client.messages.list()[-2]

        if not is_tag(last_message):
            train(model, last_message, get_tag(this_message))

    else:
        send_to = (this_message.From == my_number) ? other_number : my_number

        message = client.messages.create(
            body= message.body 
            to= send_to 
            from_="+18582155230"
        )

# Forwards call to other person
@app.route("/forward"  methods=['GET' 'POST'])
def forward():
    from_number = request.values.get('PhoneNumber'  None)
    send_to = (from_number == my_number) ? other_number : my_number

    resp = twiml.Response()
    with resp.dial() as r:
        r.number(send_to)

    return str(resp)


def is_tag(message):
    return "tag:" in message.body

def get_tag(message):
    return message.body.strip()[-1]

def train(model, body, tag):
    # Do some nlp stuff on the body
    pass


if __name__ == "__main__":
    app.run()