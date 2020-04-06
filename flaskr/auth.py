# File for managing user login, creation and sessions

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flaskr.models import User

app = Flask(__name__)

login = LoginManager()

login.init_app(app)

test_pass = 'ThisIsATest'
print(test_pass)
hash = generate_password_hash(test_pass)
print(hash)
hash2 = generate_password_hash(test_pass)
print(hash2)

@login_manager.user_loader
def load_user(user_id):
    print()


# Verifies that the account is available
def verify_account(firstname, lastname, useername, email, password):
    print()


# Verifies that the user account is available and creates the account if available
def create_new_account(firstname, lastname, useername, email, password):
    print()


# Validates that the entered password matches the stored hash value
def login(password):
    return check_password_hash(hash, test_pass)

