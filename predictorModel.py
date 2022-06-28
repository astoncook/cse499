# Imports
import yfinance
import plotly.graph_objs
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from datetime import date, timedelta


def predictor(ticker, numberDays):
    # range of days to predict
    dateTime = yfinance.download(ticker, period='30d')
    dateTime.reset_index(inplace=True)
    dateTime['Day'] = dateTime.index

    # create a new column with the date of the day
    days = list()
    for i in range(len(dateTime.Day)):
        days.append([i])

    X = days
    Y = dateTime[['Close']]

    # split the data into training and testing sets
    xAxis, x_test, yAxis, y_test = train_test_split(
        X, Y, test_size=0.1, shuffle=False)

    # create and fit the model
    gridSearch = GridSearchCV(
        estimator=SVR(kernel='rbf'),
        param_grid={
            'C': [0.001, 0.01, 0.1, 1, 100, 1000],
            'epsilon': [
                0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10,
                50, 100, 150, 1000
            ],
            'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5, 8, 40, 100, 1000]
        },
        cv = 5,
        scoring = 'neg_mean_squared_error',
        verbose = 0,
        n_jobs = -1)

    # fit the model
    yAxis = yAxis.values.ravel()
    yAxis
    gridExpect = gridSearch.fit(xAxis, yAxis)
    best_params = gridExpect.best_params_
    efficientModel = SVR(kernel='rbf',
                         C=best_params["C"],
                         epsilon = best_params["epsilon"],
                         gamma = best_params["gamma"],
                         max_iter =- 1)

    # Regression Models
    regressionModel = efficientModel

    regressionModel.fit(xAxis, yAxis)

    # make predictions on the testing set
    numberOfDays = list()
    for i in range(1, numberDays):
        numberOfDays.append([i + x_test[-1][0]])

    dates = []
    current = date.today()
    for i in range(numberDays):
        current += timedelta(days=1)
        dates.append(current)

    # make predictions on the testing set
    fig = plotly.graph_objs.Figure()
    fig.add_trace(
        plotly.graph_objs.Scatter(
            x=dates,
            y=regressionModel.predict(numberOfDays),
            mode='lines+markers',
            name='data'))
    fig.update_layout(
        title="Predicted Close Price of next " + str(numberDays - 1) + " days",
        xaxis_title="Date",
        yaxis_title="Closed Price",
    )

    return fig
