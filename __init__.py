# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
#
# app = Flask(__name__)
#
# # create and configure the app
# app.config.from_mapping(
#     SECRET_KEY='dev',
#     ENV='development',
#     # Database connection definition
#     SQLQLCHEMY_DATABASE_URL="sqlite:////users.db",
#     # Tells the database to note track any modifications
#     # Reduces overhead
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )
#
# loginmanager = LoginManager()
# loginmanager.init_app(app)
#
# db = SQLAlchemy()
#
# def create_app():