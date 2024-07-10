from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

EXCHANGE_RATE_SERVICE_URL = 'http://exchange_rate_service:5001/rates'

def get_rates():
    response = requests.get(EXCHANGE_RATE_SERVICE_URL)
    return response.json()

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    amount = data['amount']
    from_currency = data['from_currency']
    to_currency = data['to_currency']
    
    rates = get_rates()
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    
    result = amount * rates[to_currency]
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
