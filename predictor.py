import dash
from dash import dcc
from dash import html
from datetime import datetime as dt
import yfinance as yf
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from sklearn.svm import SVR
from predictorModel import prediction

# load the data
app = dash.Dash(
    __name__,)
server = app.server
app.layout = html.Div(
    [
        html.Div(
            [
                # Navigation
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
                    dcc.Input(id="number_days",
                              type="text",
                              placeholder="number of days"),
                    html.Button(
                        "prediction", className="prediction-btn", id="prediction")
                ],
                         className="buttons"),
            ],
            className="nav"),

        # content
        html.Div(
            [
                html.Div(
                    [  # header
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
              [Input("prediction", "n_clicks")],
              [State("number_days", "value"),
               State("stockTicker", "value")])

def stockPrediction(n, number_days, val):
    if n == None:
        return [""]
    if val == None:
        raise PreventUpdate
    fig = prediction(val, int(number_days) + 1)
    return [dcc.Graph(figure=fig)]


if __name__ == '__main__':
    app.run_server()