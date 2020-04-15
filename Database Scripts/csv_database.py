#Script to retreive data from our Azure Database and download as CSV

import sys
import json
import csv
import pyodbc



#SQL Database Connection
server = 'tcp:sa-server2.database.windows.net'
database = 'StockAdviseDB'
username = 'adminSA'
password = 'stock-123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print(cursor)



# *************Import Data From MAIN as CSV***************************************
all = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
cursor.execute(all)
fetch = cursor.fetchall()
cursor.commit()

#This iterates through all the rows of data and prints on console
with open('main.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in fetch:
        w.writerow(i)
        print('row')
