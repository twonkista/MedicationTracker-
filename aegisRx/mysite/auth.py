from flask import Flask, Blueprint, render_template, session, redirect, request
import pyrebase
auth = Blueprint('auth', __name__)

config ={
    "apiKey": "AIzaSyDzB9AORkJQSKSnI1wZaMX0BXrkgl75SNA",
    "authDomain": "aegisr-d8561.firebaseapp.com",
    "projectId": "aegisr-d8561",
    "storageBucket": "aegisr-d8561.appspot.com",
    "messagingSenderId": "709511623951",
    "appId": "1:709511623951:web:2e8d4a6ebc674900b9ba7a",
    "measurementId": "G-5JPQGY471T",
    "databaseURL":''
}

firebase = pyrebase.initialize_app(config)
log = firebase.auth()


@auth.route('/login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(username,password)
        except:
            return render_template('index.html')
    return render_template('dashboard.html')

@auth.route('/logout')
def logout():
    return 'logout'

@auth.route('/register')
def register():
    return 'register'