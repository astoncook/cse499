from dash import dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from predictorModel import predictor
#from flask import Flask, jsonify, request

#tried to use flask to get the data from the frontend, but it didn't work.
#app = Flask(__name__, static_folder='')

#@app.route('/', methods=['GET'])
#def home():
#    return app.send_static_file('stockInformation.html')


# load the data into dash to display the chart
app = dash.Dash(
    __name__,)
server = app.server
app.layout = html.Div(
    [
        #All of the html because flask wasn't working.
        html.Div(
            [
                html.P("Stock Predictor", className="start"),
                html.Div([
                    html.P("Input stock ticker: "),
                    html.Div([
                        dcc.Input(id="stockTicker", type="text"),
                    ],
                        className="form")
                ],
                    className="inputPlace"),

                html.Div([
                    dcc.Input(id="numberDays",
                              type="text",
                              placeholder="number of days"),
                    html.Button(
                        "predictor", className="prediction", id="predictor")
                ],
                    className="buttons"),
            ],
            className="nav"),

        html.Div(
            [
                html.Div(
                    [
                        html.Img(id="logo"),
                        html.P(id="ticker")
                    ],
                    className="header"),
                html.Div(id="description", className="ticker"),
                html.Div([], id="graphsContent"),
                html.Div([], id="mainContent"),
                html.Div([], id="predictionContent")
            ],
            className="content"),
    ],
    className="container")

# Get the prediction and the graph
@app.callback([Output("predictionContent", "children")],
              [Input("predictor", "n_clicks")],
              [State("numberDays", "value"),
               State("stockTicker", "value")])

# Define the stock prediction into the number of days entered
def stockPrediction(number, numberDays, value):
    if number == None:
        return [""]
    if value == None:
        raise PreventUpdate
    fig = predictor(value, int(numberDays) + 1)
    return [dcc.Graph(figure=fig)]


if __name__ == '__main__':
    app.run_server()