from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Medication(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    drug_name = db.Column(db.String(100))
    reason = db.Column(db.String(250))
    isTaken = db.Column(db.Boolean,default=False,nullable=False)
    start_date = db.Column(db.DateTime(timezone=True),default=func.now())
    freq_in_Days = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    meds = db.relationship('Medication')
