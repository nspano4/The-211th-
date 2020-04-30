# File for managing user login, creation and sessions

from flask import Flask
import re
from werkzeug.security import generate_password_hash


app = Flask(__name__)


# Verifies that the information entered is valid using regexes
def verify_information(firstname, lastname, username, email, password):
    # Validate the email
    # Logic :  Anything before an @ and anything after ending
    # with either '.net', '.com' or '.edu'
    #
    # This can accept wrong information at the end but it's a quick fix
    # Ex g@s.edu is valid
    # Max length 50
    if(re.fullmatch("([A-Za-z0-9].*@..*\.(com|net|edu)){10,50}", email)):
        # validate the username
        # Logic : anything between 4 and 20 characters
        # and only alphanumeric characters including underscores
        if(re.fullmatch('[A-Za-z0-9]{4,25}', username)):
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
