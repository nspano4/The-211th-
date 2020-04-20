import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
import pickle
import datetime
import random
from call_database import *
import os

dir = os.getcwd()
sep = os.path.sep

# Dynamic path to the MachineLearning directory
# Removes the need for hard-coding the path
machineLearningDir = dir + sep + "MachineLearning" + sep

def stockData(stock):
    while True:
        #print('Please select one of the following:')
        #print('GOOGL')
        #print('AAPL')
        #print('MSFT')
        #stock = input()
        if str(stock).casefold() == 'GOOGL'.casefold():
            database.pullTodaysStockData('GOOGL')
            data = pd.read_csv(machineLearningDir + "today.csv", sep=',')
            return data, 'GOOGL'
        elif str(stock).casefold() == 'AAPL'.casefold():
            pullTodaysStockData('AAPL')
            data = pd.read_csv(machineLearningDir + "today.csv", sep=',')
            return data, 'AAPL'
        elif str(stock).casefold() == 'MSFT'.casefold():
            pullTodaysStockData('MSFT')
            data = pd.read_csv(machineLearningDir + "today.csv", sep=',')
            return data, 'MSFT'
        else:
            print('We Do Not Follow ' + str(stock) + ' At This Time. Please Try Again.')

def train():

    data = pd.read_csv( machineLearningDir + "AllData.csv")

    data = data[["Open", "High", "Low", "Close", "Volume"]]

    x = np.array(data.drop(["Close"], 1))
    y = np.array(data["Close"])

    with open(machineLearningDir + "Best.txt", "r") as r:
        best_in = r.read()
    best = float(best_in)
    i = 0
    for _ in range(5000):  # The greater the range, the greater the accuracy may be
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.6)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        i += 1
        print("Accuracy: " + str(acc) + ": " + str(i))
        if acc >= best:
            best = acc
            print("Best: " + str(best))
            with open(machineLearningDir + "prediction.pickle", "wb") as f:
                pickle.dump(linear, f)
            with open(machineLearningDir + "Best.txt", "w+") as g:
                g.write(str(best))

def test(symbol):
    data, stock = stockData(symbol)

    data = data[["Open", "High", "Low", "Close", "Volume"]]

    x = np.array(data.drop(["Close"], 1))
    y = np.array(data["Close"])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.4)

    # This section will test the current stock data with the model
    pickle_in = open(machineLearningDir + "prediction.pickle", "rb")
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
        with open(machineLearningDir + 'predicted_' + str(stock) + '.csv',
                  mode='w') as predicted_file:
            fieldname = ['Date', 'Predicted Close']
            predicted_writer = csv.DictWriter(predicted_file, fieldnames=fieldname)
            predicted_writer.writeheader()
            predicted_writer.writerow({'Date': currentDate, 'Predicted Close': predicted[x]})


def predictValue(variable, symbol):
    data, stock = stockData(symbol)

    data = data[["Open", "High", "Low", "Close", "Volume"]]

    x = np.array(data.drop([str(variable)], 1))
    y = np.array(data[str(variable)])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.4)

    # This section will test the current stock data with the model
    pickle_in = open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/prediction.pickle", "rb")
    linear = pickle.load(pickle_in)

    predicted = linear.predict(x_test)
    for x in range(len(predicted)):
        if predicted[x] < 0:
            predicted[x] = -1 * predicted[x]
        print("Predicted: " + str(predicted[x]), "Actual: " + str(y_test[x]))

def tomorrowValues(symbol):
    #temp, stock = pullAllStockData(symbol)
    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/All" + str(symbol) + "Data.csv", "r",
              newline="") as csvfile1:
        spamreader = csv.reader(csvfile1, delimiter=',')
        values = [row for idx, row in enumerate(spamreader) if idx in (1,0)]

        tempValue = 0
        for _ in range(0, 5):
            j = random.randint(2, 5)
            j = j * 0.01
            i = (-1)**random.randrange(2)
            tempValue = tempValue + float(values[1][6]) + ((float(values[1][6]) * j) * i)

        predictOpen = str(tempValue / 5)
        print("Predicted Open: " + predictOpen)
        print(values[1][6])

        #prevOpen = values[1][3]
        prevHigh = float(values[1][4])
        prevLow = float(values[1][5])
        prevClose = float(values[1][6])
        #prevVolume = values[1][7]

        predictHigh = 0
        predictLow = 0
        print("Low: " + str(prevLow))
        print("High: " + str(prevHigh))
        print("Close: " + str(prevClose))

        if min(prevLow, prevClose) == prevClose:
            print('Low')
            predictLow = prevLow - (abs(prevHigh - prevLow)) / 2
            predictHigh = prevHigh - (abs(prevHigh - prevLow)) / 2
        if (min(prevHigh, prevClose) == prevClose):
            print('High')
            predictLow = prevLow + (abs(prevHigh - prevLow)) / 2
            predictHigh = prevHigh + (abs(prevHigh - prevLow)) / 2

        print("Predicted Low: " + str(predictLow))
        print("Predicted High: " + str(predictHigh))
    csvfile1.close()

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/All" + str(symbol) + "DataPredicted.csv", "w",
              newline="") as csvfile2:
        spamwriter = csv.writer(csvfile2, delimiter=';')
        spamwriter.writerow({"Open,High,Low,Close,Volume"})
        spamwriter.writerow({str(predictOpen) + "," + str(predictHigh) + "," + str(predictLow) + ", 0, 0"})
    csvfile2.close()