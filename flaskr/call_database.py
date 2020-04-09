# Script to retrieve data from our Azure Database

import os
import sys
import json
import pyodbc

server = os.getenv('DBURL')
database = os.getenv('DBNAME')
username = os.getenv('DBUSER')
password = os.getenv('DBPASS')

# SQL Database Connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER='+ server +
                      ';DATABASE='+ database +
                      ';UID='+ username +
                      ';PWD='+ password)
cursor = cnxn.cursor()
# print(cursor)

# All select statement retrieves data from our main historical data table
main = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
stocks = "SELECT * FROM StockAdviseDB.dbo.StockID"
usersQuery = "SELECT * FROM StockAdviseDB.dbo.Users"
emailQuery = "SELECT EMAIL FROM StockAdviseDB.dbo.Users"
usernameQuery = "SELECT USERNAME FROM StockAdviseDB.dbo.Users"


# Prints the stock information into the console
def print_stocks():
    cursor.execute(main)
    fetch = cursor.fetchall()
    cursor.commit()
    # This iterates through all the rows of data and prints on console
    for i in fetch:
        # To get specific values from columns, index the lists
        # For example, to get just the dates, print(i[2])
        print(i)


# Gathers all the stock information
def return_stocks():
    cursor.execute(main)
    fetch = cursor.fetchall()
    cursor.commit()
    stocks = ""
    for row in fetch:
        # 'str(row)' tell the program to treat 'row' as a string variable
        # Program treats is as a row instance otherwise and throws an error
        stocks = stocks + str(row) + '\n'
    return stocks


# Prints out the user rows
def print_users():
    cursor.execute(usersQuery)
    fetch = cursor.fetchall()
    cursor.commit()
    for row in fetch:
        print(row)


# Check if the email is already in the database
def check_email(email):
    query = emailQuery + " WHERE EMAIL = " + email
    cursor.execute(query)
    cursor.fetchall()
    if(cursor.rowcount > 0):
        return False
    else:
        return True


# Check if the email is already in the database
def check_username(username):
    query = username + " WHERE USERNAME = " + username
    cursor.execute(query)
    cursor.fetchall()
    if(cursor.rowcount > 0):
        return False
    else:
        return True
