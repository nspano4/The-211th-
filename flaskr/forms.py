from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import regexp, InputRequired, Email
import uuid


# Form for user login
class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired('Username is required'),
        regexp('[A-Za-z0-9]{2,20}')
    ])
    password = PasswordField('password', validators=[
        InputRequired('Password is required'),
        regexp('[A-Za-z0-9_!@#$%^&*?]{7,20}')
    ])
    submit = SubmitField('Sign In')


# Form for user registration
class RegistrationForm(FlaskForm):

    username = StringField('username', validators=[
        InputRequired('Username is required'),
        regexp('[A-Za-z0-9]{4,20}'),
    ])
    password = PasswordField('password', validators=[
        InputRequired('Password is required'),
        regexp('[A-Za-z0-9_!@#$%^&*?]{7,20}')
    ])
    email = StringField('email', validators=[
        InputRequired('Email is required'),
        regexp('[A-Za-z0-9].*@..*\.(com|net|edu){10,50}'),
        Email("Enter a valid email address")
    ])
    firstname = StringField('firstName', validators=[
        InputRequired('First Name is required'),
        regexp('[A-za-z]{2-20}')
    ])
    lastname = StringField('lastName', validators=[
        InputRequired('Last Name is required'),
        regexp('[A-Za-z]{2,20}')
    ])
    submit = SubmitField('Sign In')
