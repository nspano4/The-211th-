from flask import Flask, render_template, redirect, flash, request, url_for
from flask_socketio import SocketIO
from flaskr.forms import LoginForm, RegistrationForm
from flaskr.db import db
import os
from flaskr.config import Config

app = Flask(__name__, instance_relative_config=True)
sep = os.path.sep
app.config.from_object(Config)

socketio = SocketIO(app, cors_allowed_origins='*')

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Checks that the database is created
if not (os.path.exists(os.getcwd() + sep + 'flaskr' + sep + 'database.db')):
    print(1)
    db.create_all()
    print(2)

# Home page route
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/services")
def services():
    return render_template("services.html")


# Route for the products page
@app.route("/products")
def products():
    return render_template("products.html")


# Route for the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if(request.method == 'POST'):
        print('Login request')
        # Checks the the information in the form is valid
        if(form.validate_on_submit()):
            print('valid')
            flash("Login request for user {}".format(form.username.data))
            return redirect(url_for('home'))
        print('invalid')
        return render_template("login.html", form=form)
    else:
        return render_template("login.html", form=form)


# Route for the register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if(request.method == 'POST'):
        print('Register request')
        # Checks that the information in the form is valid
        if(form.validate_on_submit()):
            print("valid")
            flash('User {} registered'.format(form.username.data))
            return redirect(url_for('login'))
        print("invalid")
        return render_template("register.html", form=form)
    else:
        return render_template("register.html", form=form)


# Route for 500 errors
@app.errorhandler(500)
def database_error(e):
    return "500 Error page"


# Route for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return "404 Error page"

if(__name__=="__main__"):
    # app.run(host=='0.0.0.0', port=5000)
    socketio.run(app, host='127.0.0.1', port=5000)
