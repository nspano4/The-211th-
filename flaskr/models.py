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
    pass_hash = db.Column(db.String(100))
    username = db.Column(db.String(25))

    # Functions to return values
    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def get_pass_hash(self):
        return self.pass_hash

    def get_username(self):
        return self.username

    def get(self):
        return self


# Database entries for the daily stock report entries
class StockEntryDay(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(6))
    date = db.Column(db.String(10))
    open_val = db.Column(db.Float)
    close_val = db.Column(db.Float)
    high_val = db.Column(db.Float)
    lov_val = db.Column(db.Float)
    volume = db.Column(db.Integer)

    # Functions to return values
    def get_stock_id(self):
        return self.stock_id

    def get_symbol(self):
        return self.symbol

    def get_date(self):
        return self.date

    def get_open(self):
        return self.open_val

    def get_close(self):
        return self.close_val

    def get_high(self):
        return self.high_val

    def get_low(self):
        return self.lov_val

    def get_vol(self):
        return self.volume


# Database model for the stock entries
class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(6))

    # Functions to return values
    def get_stock_id(self):
        return self.stock_id

    def get_symbol(self):
        return self.symbol
