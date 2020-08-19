from messages import send
from flask import Flask
import os
app = Flask(__name__)

@app.route('/compliment/<phone_number>')
def compliment(phone_number):
    send.compliment(phone_number)
    db_url = os.getenv('DB_URL')
    return f'Thanks for stopping by, we are sending {phone_number} a compliment now! db_url={db_url}'

@app.route('/greeting/<phone_number>')
def greeting(phone_number):
    send.greeting(phone_number)
    db_url = os.getenv('DB_URL')
    return f'Thanks for stopping by, we are sending {phone_number} a greeting now! db_url={db_url}'