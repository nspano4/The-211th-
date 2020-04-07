import csv
import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
import pickle
import datetime
from call_database import *


def stockData():
    while True:
        print('Please select one of the following:')
        print('GOOGL')
        print('AAPL')
        print('MSFT')
        stock = input()
        if str(stock).casefold() == 'GOOGL'.casefold():
            pullTodaysStockData('GOOGL')
            data = pd.read_csv("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/today.csv", sep=',')
            return data, 'GOOGL'
        elif str(stock).casefold() == 'AAPL'.casefold():
            pullTodaysStockData('AAPL')
            data = pd.read_csv("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/today.csv", sep=',')
            return data, 'AAPL'
        elif str(stock).casefold() == 'MSFT'.casefold():
            pullTodaysStockData('MSFT')
            data = pd.read_csv("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/today.csv", sep=',')
            return data, 'MSFT'
        else:
            print('We Do Not Follow ' + str(stock) + ' At This Time. Please Try Again.')

def train():
    data = pd.read_csv("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/^DJI.csv")

    data = data[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]

    x = np.array(data.drop(["Close", "Adj Close"], 1))
    y = np.array(data["Close"])

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/Best.txt", "r") as r:
        best_in = r.read()
    best = float(best_in)
    i = 0
    for _ in range(5000):  # The greater the range, the greater the accuracy may be
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        i += 1
        print("Accuracy: " + str(acc) + ": " + str(i))
        if acc >= best:
            best = acc
            print("Best: " + str(best))
            with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/prediction.pickle", "wb") as f:
                pickle.dump(linear, f)
            with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/Best.txt", "w+") as g:
                g.write(str(best))

def test():
    data, stock = stockData()#pd.read_csv("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/today.csv", sep=';')

    data = data[["Open", "High", "Low", "Close", "Volume"]]

    x = np.array(data.drop(["Close"], 1))
    y = np.array(data["Close"])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    # This section will test the current stock data with the model
    pickle_in = open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/prediction.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("-------------------------")
    print('Coefficient: \n', linear.coef_)
    print('Intercept: \n', linear.intercept_)
    print('Accuracy: \n', 100 + linear.intercept_)
    print("-------------------------")

    predicted = linear.predict(x_test)
    for x in range(len(predicted)):
        if predicted[x] < 0:
            predicted[x] = -1 * predicted[x]
        print("Predicted: " + str(predicted[x]), "Actual: " + str(y_test[x]))
        currentDate = datetime.datetime.now().date()
        currentDate = str(currentDate)
        with open('C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/predicted_' + str(stock) + '.csv',
                  mode='w') as predicted_file:
            fieldname = ['Date', 'Predicted Close']
            predicted_writer = csv.DictWriter(predicted_file, fieldnames=fieldname)
            predicted_writer.writeheader()
            predicted_writer.writerow({'Date': currentDate, 'Predicted Close': predicted[x]})
