from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskr.config import Config

app = Flask(__name__)

# create and configure the app
app.config.from_object(Config)

loginmanager = LoginManager()
loginmanager.init_app(app)

db = SQLAlchemy(app)
