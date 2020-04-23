from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flaskr.config import Config
from flaskr.db import load_user

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize the app
    db.init_app(app)

    # Initializes the user loader for logins
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    # Initializes the routes in the endpoints file
    from flaskr.endpoints import routes
    app.register_blueprint(routes)

    return app
