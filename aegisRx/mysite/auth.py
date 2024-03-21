from flask import Blueprint,render_template, request, flash,redirect,url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('SUIIIII!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('7-1 Bitch',category='error')
        else:
            flash('no bitches detected',category='error')
    return render_template('login.html',user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        phone_number = request.form.get('phonenumber')
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('exista alreasy')
        if len(username) < 4:
            flash('bad',category='error')
        elif len(password) < 7:
            flash('bad',category='error')
        elif len(phone_number) < 9:
            flash('bad',category='error')
        else:
            new_user = User(username = username, phone_number = phone_number, password = generate_password_hash(password, method='scrypt', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!',category='success')
            return redirect(url_for('views.dashboard'))

    return render_template('signup.html')