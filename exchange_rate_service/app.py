from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

@app.route('/rates', methods=['GET'])
def get_rates():
    response = requests.get(URL)
    data = response.json()
    
    if response.status_code != 200:
        return jsonify({'error': 'Error en el cambio'}), response.status_code
    
    return jsonify(data['conversion_rates'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
