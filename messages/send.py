# send.py
import logging, requests, json

def compliment(phone_number):
    print('compliment', phone_number)

def greeting(phone_number):
    print('greeting', phone_number)

    url = 'http://localhost:8069/api/crm.lead/1'
    # data = json.loads('')

    resp = requests.get(
        url = url,
        headers = {'Access-Token': 'a9a4030acc3d6aaf753e1b0228af3f1d2f04e931'},
    )
    print(resp.json())