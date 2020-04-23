
from flask import Flask, render_template, redirect, flash, request, url_for, Blueprint
import uuid
from flaskr import db

from flaskr.forms import LoginForm, RegistrationForm
from flaskr.db import User
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
sep = os.path.sep

routes = Blueprint('routes', __name__)

# Home page route
@app.route("/")
def home():
    print(db.session.query(User).first())
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
    # If the user is trying to log in
    if(request.method == 'POST'):
        print('Login request')
        # Checks the the information in the form is valid
        if(form.validate_on_submit()):
            print('valid')
            flash("Login request for user {}".format(form.username.data))
            return redirect(url_for('home'))
        print('invalid')
        return render_template("home.html", form=form)
    # If the user is opening the webpage
    else:
        return render_template("login.html", form=form)


# Route for the register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    # If the user is trying to register
    if(request.method == 'POST'):
        print('Register request')
        # Checks that the information in the form is valid
        if(form.validate_on_submit()):
            print("valid")
            try:
                # Add the user account into the database
                db.session.add(User(id=uuid.uuid3(),
                                    first_name=form.firstname,
                                    last_name=form.lastname,
                                    email=form.email,
                                    username=form.username,
                                    pass_hash=generate_password_hash(form.password)))
                db.session.commit()
                flash('User {} registered'.format(form.username.data))
                return redirect(url_for('login'))
            except:
                return "There was am issue registering you"
        print("invalid")
        flash("Invalid user account")
        return render_template("register.html", form=form)
    # If the user is visiting the webpage
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

@app.route('/add/<user:id>')
def add_user(form):
    print('Add user endpoint in development')

@app.route('/delete/<user:id>')
def delete_user():
    print('Delete user endpoint in development')


