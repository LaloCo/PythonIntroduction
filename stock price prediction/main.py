import csv, os
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from datetime import datetime

open_prices = []
prices = []

def get_data(filename):
    os.chdir("stock price prediction")
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            open_prices.append(float(row[1]))
            prices.append(float(row[5]))
    return

def predict_prices(open_prices, prices, x):
    open_prices = np.reshape(open_prices, (len(open_prices), 1))

    svr_lin = SVR(kernel='linear', C=1000.0)
    #svr_poly = SVR(kernel='poly', C=1000.0, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1000.0, gamma=0.1)

    # Train
    svr_lin.fit(open_prices, prices)
    #svr_poly.fit(open_prices, prices)
    svr_rbf.fit(open_prices, prices)

    # Predict and Plot
    plt.scatter(open_prices, prices, color='black', label='Data')
    plt.plot(open_prices, svr_lin.predict(open_prices), color='red', label='Linear model')
    #plt.plot(open_prices, svr_poly.predict(open_prices), color='green', label='Polynomial model')
    plt.plot(open_prices, svr_rbf.predict(open_prices), color='blue', label='RBF model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    #return svr_lin.predict(x)[0], svr_poly.predict(x)[0], svr_rbf.predict(x)[0]
    return svr_lin.predict(x)[0], svr_rbf.predict(x)[0]

get_data('TSLA.csv')
predicted_prices = predict_prices(open_prices, prices, 300.0)

print(predicted_prices)