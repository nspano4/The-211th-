from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():

    app = Flask(__name__)
    # Points where to look for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    # Tells the app to not track anll the modifications to the database
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    from flaskr.endpoints import routes

    app.register_blueprint(routes)

    return app