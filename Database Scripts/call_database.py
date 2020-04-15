#Script to retreive data from our Azure Database

import sys
import json
import pyodbc



#SQL Database Connection
server = 'tcp:sa-server2.database.windows.net'
database = 'StockAdviseDB'
username = 'adminSA'
password = 'stock-123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print(cursor)



#*************GET ALL DATA***************************************
# all = "SELECT * FROM StockAdviseDB.dbo.MAIN;"
# cursor.execute(all)
# fetch = cursor.fetchall()
# cursor.commit()
#
# #This iterates through all the rows of data and prints on console
# for i in fetch:
#     #To get specific values from columns, index the lists
#     #For example, to get just the dates, print(i[2])
#     print(i)


#****************GET DATA FOR A SINGLE STOCK**********************

#Type in the symbol for what data you want
symbol = 'MSFT'

#This calls the data for whatever symbol you have set to that variable above
query = "SELECT * FROM StockAdviseDB.dbo.MAIN WHERE SYMBOL = '%s';" % symbol
cursor.execute(query)
fetch = cursor.fetchall()
cursor.commit()

for i in fetch:
    print(i)
