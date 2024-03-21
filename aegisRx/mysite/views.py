from flask import Blueprint, render_template, request,flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Medication
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/home')
def homeback():
    return render_template('index.html')

@views.route('/login',methods=['GET','POST'])
def signin():
    return render_template('login.html')

@views.route('/signupPage')
def signup():
    return render_template('signup.html')

@views.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        drug = request.form.get('meds')
        reason = request.form.get('reason')
        freq = request.form.get('freqdays')


        newMed = Medication(drug_name = drug, reason = reason,freq_in_Days = freq,user_id = current_user.id)
        db.session.add(newMed)
        db.session.commit()
    return render_template('dashboard.html',user=current_user)
