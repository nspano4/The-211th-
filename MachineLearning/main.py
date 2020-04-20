from MachineLearning.LinearRegression import *
from call_database import *

# The main class will allow you to test some of the functionality of our project.
def main():
    tomorrowValues("AAPL")
    #pullAllData()
    #pullTodaysStockData("GOOGL")
    #pullAllStockData("GOOGL")
    #train()
    #while True:
    test("AAPL")
    predictValue("Close", "MSFT")




if __name__ == "__main__":
    main()