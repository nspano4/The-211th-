#Script to retreive data from our Azure Database

import sys
import json
import pyodbc
import csv

#*************GET ALL DATA***************************************
def pullAllData():
    all = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
    cursor.execute(all)
    fetch = cursor.fetchall()
    cursor.commit()
# #This iterates through all the rows of data and prints on console
    for i in fetch:
        #To get specific values from columns, index the lists
        #For example, to get just the dates, print(i[2])
        print(i)

#****************GET DATA FOR A SINGLE STOCK**********************
def pullTodaysStockData(symbol):
    #Type in the symbol for what data you want
    #symbol = 'MSFT'
    #This calls the data for whatever symbol you have set to that variable above
    query = "SELECT * FROM StockAdviseDB.dbo.MAIN WHERE SYMBOL = '%s';" % symbol
    #all = "SELECT * FROM StockAdviseDB.dbo.MAIN WHERE SYMBOL = 'MSFT' order by DATE desc"

    cursor.execute(query)
    fetch = cursor.fetchall()
    cursor.commit()

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/testme.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= ';')
        for i in fetch:
            spamwriter.writerow(i)
        csvfile.close()

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/testme.csv", "r", newline="") as csvfile1:
        with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/today.csv", "w",
                  newline="") as csvfile2:
            spamreader = csv.reader(csvfile1, delimiter=';')
            row1 = next(spamreader)
            stringRow1 = str(row1)
            newString = stringRow1.replace("\'", "")
            newString = newString.replace("[", "")
            newString = newString.replace("]", "")
            spamwriter = csv.writer(csvfile2, delimiter=';')
            spamwriter.writerow({"Index,Stock,Date,Open,High,Low,Close,Volume"})
            spamwriter.writerow({newString})

def pullAllStockData(symbol):
    #Type in the symbol for what data you want
    #symbol = 'MSFT'
    #This calls the data for whatever symbol you have set to that variable above
    query = "SELECT * FROM StockAdviseDB.dbo.MAIN WHERE SYMBOL = '%s';" % symbol

    cursor.execute(query)
    fetch = cursor.fetchall()
    cursor.commit()

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/testme.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= ';')
        for i in fetch:
            spamwriter.writerow(i)
        csvfile.close()

    with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/testme.csv", "r", newline="") as csvfile1:
        with open("C:/Users/Ethan Hudak/PycharmProjects/The-211th-/MachineLearning/All" + str(symbol) + "Data.csv", "w",
                  newline="") as csvfile2:
            spamreader = csv.reader(csvfile1, delimiter=';')
            spamwriter = csv.writer(csvfile2, delimiter=';')
            spamwriter.writerow({"Index,Stock,Date,Open,High,Low,Close,Volume"})
            row1 = next(spamreader)
            for _ in spamreader:
                stringRow1 = str(row1)
                newString = stringRow1.replace("\'", "")
                newString = newString.replace("[", "")
                newString = newString.replace("]", "")
                spamwriter.writerow({newString})


#SQL Database Connection
server = 'tcp:sa-server2.database.windows.net'
database = 'StockAdviseDB'
username = 'adminSA'
password = 'stock-123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
