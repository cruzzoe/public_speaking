from datetime import datetime
from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    account_type = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    dogs = db.relationship('Dog', backref='owner', lazy='dynamic')
    booking_slot = db.relationship('Slot', backref='booker', lazy='dynamic')
    blast_recipients = db.relationship('BlastConfig', backref='blast_owner', lazy='dynamic')

class Session():
    pass

class Speech():
    pass

