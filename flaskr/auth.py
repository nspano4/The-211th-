# File for managing user login, creation and sessions

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

test_pass = 'ThisIsATest'
print(test_pass)
hash = generate_password_hash(test_pass)
print(hash)
hash2 = generate_password_hash(test_pass)
print(hash2)

# Verifies that the user account is available and creates the account if available
def create_new_account(firstname, lastname, useername, email, password):
    print()

# Validates that the entered password matches the stored hash value
def login(password):
    return check_password_hash(hash, test_pass)
