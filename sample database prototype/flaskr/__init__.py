import os

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

# create and configure the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'

db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

#class Test(db.Model):
#   __tablename__ = 'Stocks'
#   __table_args__ = { 'extend_existing': True }
#   LOC_CODE = db.Column(db.ID, primary_key=True) 

class StockHistory(db.Model):
    __tablename__ = 'StockHistory'
    __table_args__ = { 'extend_existing': True }
    #LOC_CODE = db.Column(db.ID, primary_key=True)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/amazon")
def amazon():
    amazonResults = StockHistory.query.filter_by(StockID='1').all()
    return render_template("amazon.html", amazon=amazonResults)

@app.route("/google")
def google():
    googleResults = StockHistory.query.filter_by(StockID='2').all()
    return render_template("google.html", google=googleResults)

@app.route("/microsoft")
def microsoft():
    msftResults = StockHistory.query.filter_by(StockID='3').all()
    return render_template("microsoft.html", msft=msftResults)
        

    
 
 
