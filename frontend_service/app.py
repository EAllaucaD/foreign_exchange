from flask import Flask, request, render_template
import requests

app = Flask(__name__)

CONVERSION_SERVICE_URL = 'http://conversion_service:5002/convert'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    
    response = requests.post(CONVERSION_SERVICE_URL, json={
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    })
    
    result = response.json()['result']
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
