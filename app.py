from messages import send
from flask import Flask
app = Flask(__name__)

@app.route('/compliment/<phone_number>')
def compliment(phone_number):
    send.compliment(phone_number)
    return f'Thanks for stopping by, we are sending {phone_number} a compliment now!'

@app.route('/greeting/<phone_number>')
def greeting(phone_number):
    send.greeting(phone_number)
    return f'Thanks for stopping by, we are sending {phone_number} a greeting now!'