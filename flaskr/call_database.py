# Script to retrieve data from our Azure Database

import os
import sys
import json
import pyodbc
import configparser

server = 'tcp:sa-server.database.windows.net'
database = 'StockAdviseDB'
username = 'adminSA'
password = 'stock-123'

# SQL Database Connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER='+ server +
                      ';DATABASE='+ database +
                      ';UID='+ username +
                      ';PWD='+ password)
cursor = cnxn.cursor()
# print(cursor)

# All select statement retreives data from our main historical data table
all = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
cursor.execute(all)
fetch = cursor.fetchall()
cursor.commit()

# Prints the stock information into the console
def print_stocks():
    # This iterates through all the rows of data and prints on console
    for i in fetch:
        # To get specific values from columns, index the lists
        # For example, to get just the dates, print(i[2])
        print(i)

# Gathers all the stock information
def return_stocks():
    stocks = ""
    for row in fetch:
        # 'str(row)' tell the program to treat 'row' as a string variable
        # Program treats is as a row instance otherwise and throws an error
        stocks = stocks + str(row) + '\n'
    return stocks
