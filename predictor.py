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
# load the data
app = dash.Dash(
    __name__,)
server = app.server
app.layout = html.Div(
    [
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
                    className="input-place"),

                html.Div([
                    dcc.Input(id="numberDays",
                              type="text",
                              placeholder="number of days"),
                    html.Button(
                        "predictor", className="prediction-btn", id="predictor")
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
                html.Div([], id="graphs-content"),
                html.Div([], id="main-content"),
                html.Div([], id="prediction-content")
            ],
            className="content"),
    ],
    className="container")

# Get the prediction and the graph
@app.callback([Output("prediction-content", "children")],
              [Input("predictor", "n_clicks")],
              [State("numberDays", "value"),
               State("stockTicker", "value")])

def stockPrediction(n, numberDays, val):
    if n == None:
        return [""]
    if val == None:
        raise PreventUpdate
    fig = predictor(val, int(numberDays) + 1)
    return [dcc.Graph(figure=fig)]


if __name__ == '__main__':
    app.run_server()