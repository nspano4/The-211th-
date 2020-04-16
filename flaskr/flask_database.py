# Script to retrieve data from our Azure Database

import os
from flask import Flask
import configparser
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import urllib


# Gets the path to root directory of the project
dir = os.getcwd()
# File separator of the OS (/ or \)
sep = os.path.sep

config = configparser.ConfigParser()
config.read(dir + sep + 'flaskr' + sep + 'config.ini')
server = config.get('config', 'server')
password = config.get('config', 'password')
username = config.get('config', 'username')
hostname = config.get('config', 'hostname')

# Dynamic path to the MachineLearning directory
# Removes the need for hard-coding the path
machineLearningDir = dir + sep + "MachineLearning" + sep

'''
server = os.getenv('DBURL')
database = os.getenv('DBNAME')
username = os.getenv('DBUSER')
password = os.getenv('DBPASS')
'''

params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};' +
                           'SERVER=' + server +
                           ';DATABASE=' + hostname +
                           ';UID=' + username +
                           ';PWD=' + password)


app = Flask(__name__)

# Accesses the database instance created in the endpoints.py file
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def get_all_stocks():
    print()

get_all_stocks()
