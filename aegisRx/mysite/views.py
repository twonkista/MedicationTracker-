from flask import Blueprint, render_template
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/home')
def homeback():
    return render_template('index.html')

@views.route('/loginPage')
def signin():
    return render_template('login.html')

@views.route('/signupPage')
def signup():
    return render_template('signup.html')
