#!/usr/bin/python -m

import os
from flask import Flask, render_template, redirect, flash
from flask_socketio import SocketIO
from flaskr.forms import LoginForm, RegistrationForm
import pyodbc
import json
from configparser import ConfigParser

# create and configure the app
app = Flask(__name__, instance_relative_config=True)


app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    FLASK_ENV='development'
)
socketio = SocketIO(app, cors_allowed_origins='*')

config = ConfigParser()

# Locates the database config file
config.read(os.getcwd() + "/config.ini")

# Reads the SQL database information from the config file
server = config.get('config', 'server')
database = config.get('config', 'hostname')
username = config.get('config', 'username')
password = config.get('config', 'password')


### CODE FOR CALLING DB AND PARSING INTO JSON OBJECT TO BE PASSED INTO JAVASCRIPT ###

cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server}'
    ';SERVER=' + server +
    ';DATABASE=' + database +
    ';UID=' + username +
    ';PWD=' + password)
cursor = cnxn.cursor()

data = []
symbol = 'MSFT'
query = "SELECT * FROM StockAdviseDB.dbo.MAIN WHERE SYMBOL = '%s';" % symbol

cursor.execute(query)
rows = cursor.fetchall()
cursor.commit()

for row in rows:
    data.append([x for x in row])
jdata = json.dumps(data, indent=4)
ndata = json.loads(jdata)

data_obj = []

for row in ndata:
    # print(row)
    dict_row = {
        'symbol': row[1],
        'date': row[2],
        'close': row[6],
    }
    data_obj.append(dict_row)

#DJSON Object for Microsoft Data
msft_data = json.dumps(data_obj, indent=4)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


#Routes to page with D3 Graphs, currently displays data as a variable
@app.route("/services")
def services():
    data = msft_data
    return render_template("services.html", data=data)


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("Login submit")
    # Checks the the information in the form is valid
    if(form.validate_on_submit()):
        flash("Login request for user {}".format(form.username.data))
        return redirect('/')
    return render_template("login.html", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print("Register submit")
    # Checks that the information in the form is valid
    if(form.validate_on_submit()):
        print("valid")
        flash('User {} registered'.format(form.username.data))
        redirect('/')
    # Passes the registration form to the page
    print("invalid")
    return render_template("register.html", form=form)


if(__name__=="__main__"):
    # app.run(host=='0.0.0.0', port=5000)
    socketio.run(app, host='127.0.0.1', port=5000)
