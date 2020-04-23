from flaskr import db

# Database model for the User entries
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.INT, primary_key=True)
    first_name = db.Column(db.VARCHAR(20))
    last_name = db.Column(db.VARCHAR(30))
    email = db.Column(db.VARCHAR(50))
    pass_hash = db.Column(db.VARCHAR(100))
    username = db.Column(db.VARCHAR(25))

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

def load_user(user_id):
    return User.query.get(user_id)

#
# # Database entries for the daily stock report entries
# class StockEntry(db.Model):
#     __tablename__ = 'StockEntry'
#     transaction_id = db.Column(db.INT)
#     symbol = db.Column(db.VARCHAR(6))
#     date = db.Column(db.VARCHAR(10))
#     open_val = db.Column(db.FLOAT)
#     high_val = db.Column(db.FLOAT)
#     low_val = db.Column(db.FLOAT)
#     close_val = db.Column(db.FLOAT)
#     volume = db.Column(db.REAL)
#
#     # Functions to return values
#     def get_stock_id(self):
#         return self.stock_id
#
#     def get_symbol(self):
#         return self.symbol
#
#     def get_date(self):
#         return self.date
#
#     def get_open(self):
#         return self.open_val
#
#     def get_close(self):
#         return self.close_val
#
#     def get_high(self):
#         return self.high_val
#
#     def get_low(self):
#         return self.low_val
#
#     def get_vol(self):
#         return self.volume
#
#
# # Database model for the stock entries
# class Stock(db.Model):
#     __tablename__ = 'StockID'
#     stock_id = db.Column(db.INT, primary_key=True)
#     symbol = db.Column(db.VARCHAR(6), unique=True)
#
#     # Functions to return values
#     def get_stock_id(self):
#         return self.stock_id
#
#     def get_symbol(self):
#         return self.symbol
#
