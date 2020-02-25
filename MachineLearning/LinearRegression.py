import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn
from sklearn.utils import shuffle
import pickle

# This section will add the data
data = pd.read_csv("LMT.csv")
#data = pd.read_csv("today.csv", sep=';')
predict = "Close"

data = data[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
#data = shuffle(data)  # Optional - shuffle the data

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# This section will use the data to train the model
with open("Best.txt", "r") as r:
    best_in = r.read()
best = float(best_in)
i = 0
for _ in range(5000): # The greater the range, the greater the accuracy may be
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    i += 1
    print("Accuracy: " + str(acc) + ": " + str(i))
    if acc >= best:
        best = acc
        print("Best: " + str(best))
        with open("prediction.pickle", "wb") as f:
            pickle.dump(linear, f)
        with open("Best.txt", "w") as g:
            g.write(str(best))

'''
# This section will test the current stock data with the model
pickle_in = open("prediction.pickle", "rb")
linear = pickle.load(pickle_in)


print("-------------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print('Accuracy: \n', 100 + linear.intercept_)
print("-------------------------")

predicted = linear.predict(x_test)
for x in range(len(predicted)):
    print(predicted[x], y_test[x])
    '''