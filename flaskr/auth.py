# File for managing user login, creation and sessions

from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
import uuid
import re
from call_database import check_email, check_username

app = Flask(__name__)

login = LoginManager()

login.init_app(app)

@login.user_loader
def load_user(user_id):
    print()


# Verifies that the information entered is valid using regexes
def verify_information(firstname, lastname, username, email, password):
    # Validate the email
    # Logic :  Anything before an @ and anything after ending
    # with either '.net', '.com' or '.edu'
    #
    # This can accept wrong information at the end but it's a quick fix
    # Ex g@s.edu is valid
    # Max length 50
    if(re.fullmatch("([A-Za-z0-9].*@..*\.(com|net|edu)){10,50}", email) and check_email(email)):
        # validate the username
        # Logic : anything between 4 and 20 characters
        # and only alphanumeric characters including underscores
        if(re.fullmatch('[A-Za-z0-9]{4,25}', username) and check_username(username)):
            # validate the password
            # Logic : Alphanumeric characters
            # and select special characters
            # Between 7 and 20 characters
            if(re.fullmatch( '[A-Za-z0-9_!@#$%^&*?]{7,20}', password)):
                # Validate the users first name
                # Logic : anything that only contains
                # alphabetic characters
                # Length between 2 and 20
                if(re.fullmatch('[a-zA-Z]{2,20}', firstname)):
                    # Validate the users last name
                    # Logic : anything that only contains
                    # alphabetic characters
                    # Length between 2 and 20
                    if(re.fullmatch('[A-Za-z]{2,20}', lastname)):
                        print('Valid user account')
                        return True
    print('Invalid user account')
    return False


'''
# Verifies that the user account is available and creates the account if available
def create_new_account(firstname, lastname, username, email, password):
    if(verify_information(firstname, lastname, username, email, password)):

        # Insert the user into the database to create the user account
        # Command is broken into multiple lines for readability
        cursor.execute('INSERT INTO ' + os.getenv('DBNAME') + '.' + os.getenv('USERS') +
                       ' (USER_ID, FIRST_NAME, LAST_NAME, EMAIL, USERNAME, PASS_HASH) VALUES ' +
                       '(\'' + str(uuid.uuid4()) + '\',' +
                       '(\'' + firstname + '\',' +
                       '(\'' + lastname + '\',' +
                       '(\'' + email + '\',' +
                       '(\'' + username + '\',' +
                       '(\'' + generate_password_hash(password) + '\')')
'''

# Validates that the entered password matches the stored hash value
def login(password):
    if check_password_hash(hash, password):
        print('Good Password')
    else:
        print('Bad Password')

'''
# Demo for the mid-assessment
def demo():
    print('Enter your firstname : ')
    firstname = str(input())
    print('Enter your lastname : ')
    lastname = str(input())
    print('Enter a username : ')
    username = str(input())
    print('Enter your email : ')
    email = str(input())
    print('Enter your a password: ')
    password = str(input())
    print()
    verify_information(firstname, lastname, username, email, password)
    test_hash = generate_password_hash(password)
    print('password hash demo  : ' + password + ' => ' + test_hash)
    print('UUID generator demo : ' + str(uuid.uuid4()))


# Demonstrate the regexes used for validating user account information
def regex_demo(firstname, lastname, username, email, password):
    if( re.fullmatch("([A-Za-z0-9].*@..*\.[cne][oed][mtu]){1,50}", email)) :
        print("Valid email")
    else:
        print('Invalid email')
    if( re.fullmatch('[A-Za-z0-9]{4,25}', username)) :
        print('Valid username')
    else:
        print('Invalid username')
    if( re.fullmatch( '[A-Za-z0-9!@#$%^&*?]{7,20}', password) ):
        print('Valid password')
    else:
        print('Invalid password')
    if( re.fullmatch('[a-zA-Z]{2,20}', firstname) ):
        print('Valid firstname')
    else:
        print('Invalid firstname')
    if( re.fullmatch('([A-Za-z]*){2,20}', lastname) ) :
        print('Valid lastname')
    else:
        print('Invalid lastname')


demo()
'''
