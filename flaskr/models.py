from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Database model for the User entries
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    pass_hash = db.Column(String(100))
    username = db.Column(String(25))


# Database entries for the daily stock report entries
class StockEntryDay(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(60))
    date = db.Column(db.String(60))
    open_val = db.Column(db.Float)
    close_val = db.Column(db.Float)
    high_val = db.Column(db.Float)
    lov_val = db.Column(db.Float)
    volume = db.Column(db.int)


# Database model for the stock entries
class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(60))
