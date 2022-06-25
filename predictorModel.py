def prediction(stock, numberDays):
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
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import GridSearchCV
    import numpy as np
    from sklearn.svm import SVR
    from datetime import date, timedelta
    # load the data

    # range of days to predict
    df = yf.download(stock, period='60d')
    df.reset_index(inplace=True)
    df['Day'] = df.index

    # create a new column with the date of the day
    days = list()
    for i in range(len(df.Day)):
        days.append([i])

    X = days
    Y = df[['Close']]

    # split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(X,
                                                        Y,
                                                        test_size=0.1,
                                                        shuffle=False)

    # create and fit the model
    gsc = GridSearchCV(
        estimator=SVR(kernel='rbf'),
        param_grid={
            'C': [0.001, 0.01, 0.1, 1, 100, 1000],
            'epsilon': [
                0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10,
                50, 100, 150, 1000
            ],
            'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5, 8, 40, 100, 1000]
        },
        cv=5,
        scoring='neg_mean_absolute_error',
        verbose=0,
        n_jobs=-1)

    # fit the model
    y_train = y_train.values.ravel()
    y_train
    grid_result = gsc.fit(x_train, y_train)
    best_params = grid_result.best_params_
    best_svr = SVR(kernel='rbf',
                   C=best_params["C"],
                   epsilon=best_params["epsilon"],
                   gamma=best_params["gamma"],
                   max_iter=-1)

    # Support Vector Regression Model for the stock prediction
    rbf_svr = best_svr

    rbf_svr.fit(x_train, y_train)

    # make predictions on the testing set
    output_days = list()
    for i in range(1, numberDays):
        output_days.append([i + x_test[-1][0]])

    dates = []
    current = date.today()
    for i in range(numberDays):
        current += timedelta(days=1)
        dates.append(current)

    # make predictions on the testing set
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=rbf_svr.predict(output_days),
            mode='lines+markers',
            name='data'))
    fig.update_layout(
        title="Predicted Close Price of next " + str(numberDays - 1) + " days",
        xaxis_title="Date",
        yaxis_title="Closed Price",
    )

    return fig