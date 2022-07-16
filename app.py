import time
from unicodedata import name
from flask import Flask, jsonify, request
import datetime
import requests
import calendar
import dateutil.relativedelta

# Flasks component that helps me run python on the server.
app = Flask(__name__, static_folder='')

# My API key (I tried to use it in my .env but it was giving me trouble).
api_key = "caibu3aad3i2a9kc4c90"

# This route gets the HTML file and sends the python logic to it in other routes.
@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('stockInformation.html')

# This route gets the company information from the .js file and api.
@app.route('/route1', methods=['GET'])
def route1():
    global name
    global finnhub_client
    name = request.args.get('CPN')

# This api gets the company information like the name, symbol, and even IPO date.
    api1 = "https://finnhub.io/api/v1/stock/profile2?symbol={}&token={}".format(
        name, api_key)
    companyInformation = requests.get(api1)
    companyInformation = companyInformation.json()
    return companyInformation

# This route gets the stock summary information from the .js file and api.
@app.route('/route2', methods=['GET'])
def quote():

# This api gets the stock summary for the day and time when activated.
    api2 = "https://finnhub.io/api/v1/quote?symbol={}&token={}".format(
        name, api_key)
    data1 = requests.get(api2)
    stock = data1.json()
    stock['t'] = time.strftime("%d %B, %Y", time.localtime(stock['t']))
    return stock

# This route gets the chart information from the .js file and api.
@app.route('/route3', methods=['GET'])
def graph():
    day2 = datetime.datetime.utcnow()
    day1 = day2 + dateutil.relativedelta.relativedelta(months=-6, days=-1)
    time1 = calendar.timegm(day1.utctimetuple())
    time2 = calendar.timegm(day2.utctimetuple())

# This api gets the candle/chart from the symbol entered.
    api3 = "https://finnhub.io/api/v1/stock/candle?symbol={}&resolution={}&from={}&to={}&token={}".format(
        name, 'D', time1, time2, api_key)
    data = requests.get(api3)
    price = data.json()

# Helps display the chart in the html file.
    new_list = []
    for i in range(len(price['t'])):
        new_list.append(
            [price['t'][i]*1000, price['c'][i], price['v'][i]])
    return jsonify(new_list)


if __name__ == "__main__":
    app.run()
