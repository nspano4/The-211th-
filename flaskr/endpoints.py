import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flaskr.forms import LoginForm, RegistrationForm

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("Login submit")
    # Checks the the information in the form is valid
    if(form.validate_on_submit()):
        flash("Login request for user {}".format(form.username.data))
        return redirect('/')
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print("Register submit")
    # Checks that the information in the form is valid
    if(form.validate_on_submit()):
        flash('User {} registered'.format(form.username.data))
        redirect('/')
    # Passes the registration form to the page
    return render_template("register.html", form=form)

if(__name__=="__main__"):
    #app.run(host=='0.0.0.0', port=5000)
    socketio.run(app, host='127.0.0.1', port=5000)
