from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Regexp


# Form for user login
class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('Sign In')


# Form for user registration
class RegistrationForm(FlaskForm):

    username = StringField('username', validators=[
        InputRequired(message='Username is required'),
        # Regexp('[A-Za-z0-9]{4,20}'),
    ])
    password = PasswordField('password', validators=[
        InputRequired(message='Password is required'),
        # Regexp('[A-Za-z0-9_!@#$%^&*?]{7,20}')
    ])
    email = StringField('email', validators=[
        InputRequired(message='Email is required'),
        # Regexp('[A-Za-z0-9].*@..*\\.(com|net|edu){10,50}'),
        Email(message="Enter a valid email address")
    ])
    firstname = StringField('firstName', validators=[
        InputRequired(message='First Name is required'),
        # Regexp('[A-za-z]{2-20}')
    ])
    lastname = StringField('lastName', validators=[
        InputRequired(message='Last Name is required'),
        # Regexp('[A-Za-z]{2,20}')
    ])
    submit = SubmitField('Register')
