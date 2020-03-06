#Script to retreive data from our Azure Database

import sys
import json
import pyodbc



#SQL Database Connection
server = 'tcp:sa-server.database.windows.net'
database = 'StockAdviseDB'
username = 'adminSA'
password = 'stock-123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print(cursor)

#ALl select statement retreives data from our main historical data table
all = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
cursor.execute(all)
fetch = cursor.fetchall()
cursor.commit()

#This iterates through all the rows of data and prints on console
for i in fetch:
    #To get specific values from columns, index the lists
    #For example, to get just the dates, print(i[2])
    print(i)
