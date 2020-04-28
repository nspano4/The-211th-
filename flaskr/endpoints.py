
from flask import Flask, render_template, redirect, flash, request, url_for, Blueprint
from flaskr.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from flaskr.models import User
from werkzeug.security import generate_password_hash
from flaskr import login_manager, db
import os

sep = os.path.sep


# Defines all the routes for the website
routes = Blueprint('routes', __name__)

# Home page endpoint
@routes.route("/")
def home():
    return render_template("home.html")


@routes.route("/about")
def about():
    return render_template("about.html")


@routes.route("/contact")
def contact():
    return render_template("contact.html")


@routes.route("/services")
def services():
    return render_template("services.html")


# Route for the products page
@routes.route("/products")
def products():
    return render_template("products.html")


# Endpoint for the login page and user login
@routes.route("/login", methods=['GET', 'POST'])
def login():
    # redirect to the home page if the user is already logged in
    if( current_user.is_authenticated ):
        return redirect(url_for('home'))
    form = LoginForm(request.form)
    # If the user is trying to log in
    if( form.validate_on_submit() ):
        print('Login request')
        # Search for the username in the database
        user = User.query.filter_by(username=form.username.data).first()
        # If the user is not found or the password is incorrect
        if( user is None or not user.check_password(form.password.data) ):
            flash('Invalid user information')
            return redirect(url_for('login'))
        # Log in the user (Only reaches here if the information is valid)
        flash("Login request for user {}".format(form.username.data))
        login_user(user)
        return redirect(url_for('home'))
    # If the user is opening the webpage
    else:
        return render_template("login.html", form=form)


# Endpoint for user logout
@routes.route('/logout')
@login_required
def logout():
    # Skip step if the user isn't logged in
    if( current_user.is_authenticated ):
        logout_user()
    redirect(url_for('home'))
    print('Logout endpoint in development')


# Route for the register page
@routes.route("/register", methods=['GET', 'POST'])
def register():
    if( current_user.is_authenticated ):
        return redirect(url_for('home'))
    form = RegistrationForm(request.form)
    # If the user is trying to register
    if( form.validate_on_submit() ):
        print('Register request')
        # Checks that the information in the form is valid
        valid = True

        if(check_for_dup_email(form.email.data)):
            valid = False
            flash('That email is already taken')
        if(check_for_dup_username(form.username.data)):
            valid = False
            flash('That username is already taken')
        if(valid):
            try:
                user = User(first_name=form.firstname.data,
                            last_name=form.lastname.data,
                            email=form.email.data,
                            username=form.username.data,
                            pass_hash=generate_password_hash(form.password.data))
                # Add the user account into the database
                db.session.add(user)
                # db.session.commit()
                flash('User {} registered'.format(form.username.data))
                db.session.commit()
                return redirect(url_for('login'))
            except:
                return "There was an issue getting you registered"
                return render_template("register.html", form=form)
    # If the user is visiting the webpage
    else:
        return render_template("register.html", form=form)


# Route for 500 errors
@routes.errorhandler(500)
def database_error(e):
    return "500 Error page"


# Route for 404 errors
@routes.errorhandler(404)
def page_not_found(e):
    return "404 Error page"


# Endpoint for user profiles
@routes.route('/profile/<user_id>')
@login_required
def profile(user_id):
    user = User.query(id=user_id).first()
    return 'Profile pages in development'

# Route for deleting a user
@routes.route('/delete/')
@login_required
def delete_user():
    print('Delete user endpoint in development')
    return'Delete user endpoint in development'


#Checks to see if there are duplicate emails
def check_for_dup_email(email):
    if(db.session.filter_by(email=email).first() == None):
        # Invalid information
        return True
    #Valid information
    return False

#Checks to see if there are duplicate emails
def check_for_dup_username(username):
    print()
    if(User.query.filter_by(username=username).first_or_404() == None):
        # Invalid information
        return True
    #Valid information
    return False