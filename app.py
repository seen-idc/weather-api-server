import time
import requests
import os
from flask import Flask, jsonify
from waitress import serve

api_key = os.getenv('API_KEY')

app = Flask(__name__)

last_api_call = {}
last_api_call_data = {}

interval = 21600

@app.route('/')
def index():
    return 'Weather API Server'

@app.route('/ruse/')
def ruse():
    query = f'https://api.openweathermap.org/data/2.5/weather?q=Carlingford,NSW,AU&appid={api_key}&units=metric&lang=en'

    if 'carlingford_nsw_au' in last_api_call:
        if time.time() - last_api_call['carlingford_nsw_au'] > interval:
            last_api_call['carlingford_nsw_au'] = time.time()
            req = requests.get(query)
            last_api_call_data['carlingford_nsw_au'] = req.text

            response = app.response_class(
                response=req.text,
                status=200,
                mimetype='application/json'
            )

            return response
        else:
            response = app.response_class(
                response=last_api_call_data['carlingford_nsw_au'],
                status=200,
                mimetype='application/json'
            )
            return response
    else:
        last_api_call['carlingford_nsw_au'] = time.time()
        req = requests.get(query)
        last_api_call_data['carlingford_nsw_au'] = req.text

        response = app.response_class(
            response=req.text,
            status=200,
            mimetype='application/json'
        )

        return response

if __name__ == "__main__":
    print('Starting server')
    serve(app, host="0.0.0.0", port=8000)