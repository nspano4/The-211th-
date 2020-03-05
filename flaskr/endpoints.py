import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)
socketio = SocketIO(app, cors_allowed_origins='*')

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/login")
def login():
    return render_template("login.html")

if(__name__=="__main__"):
    #app.run(host=='0.0.0.0', port=5000)
    socketio.run(app, host='0.0.0.0', port=5000)
