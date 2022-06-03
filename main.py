import time
from unicodedata import name
from flask import Flask, jsonify, request
import datetime
import requests
import calendar
import dateutil.relativedelta
import os
app = Flask(__name__, static_folder='')

api_key = os.environ.get('API_Key')

# Link the html


@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('stockInformation.html')

# Get the Company Information


@app.route('/test', methods=['GET'])
def test():
    global name
    global finnhub_client
    name = request.args.get('CPN')
    url1 = "https://finnhub.io/api/v1/stock/profile2?symbol={}&token={}".format(
        name, api_key)
    company = requests.get(url1)
    company = company.json()
    return company

# Get the Stock Summary


@app.route('/route2', methods=['GET'])
def quote():
    url2 = "https://finnhub.io/api/v1/quote?symbol={}&token={}".format(
        name, api_key)
    data1 = requests.get(url2)
    stock = data1.json()
    stock['t'] = time.strftime("%d %B, %Y", time.localtime(stock['t']))

    url3 = "https://finnhub.io/api/v1/stock/recommendation?symbol={}&token={}".format(
        name, api_key)
    data2 = requests.get(url3)
    return stock

# Get the stock chart


@app.route('/route3', methods=['GET'])
def graph():
    d2 = datetime.datetime.utcnow()
    d1 = d2 + dateutil.relativedelta.relativedelta(months=-6, days=-1)
    time1 = calendar.timegm(d1.utctimetuple())
    time2 = calendar.timegm(d2.utctimetuple())

    url4 = "https://finnhub.io/api/v1/stock/candle?symbol={}&resolution={}&from={}&to={}&token={}".format(
        name, 'D', time1, time2, api_key)
    data = requests.get(url4)
    candles = data.json()

    new_list = []
    for i in range(len(candles['t'])):
        new_list.append(
            [candles['t'][i]*1000, candles['c'][i], candles['v'][i]])
    return jsonify(new_list)


if __name__ == "__main__":
    app.run()
