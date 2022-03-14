from datetime import datetime
from email.policy import default
import imp
from time import timezone
from django import db
from sqlalchemy import Column, func
from flask_login import UserMixin


class Data_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(1000))
    phone = db.Column(db.String(100))
    address_user = db.Column(db.String(1000))
    nation = db.Column(db.String(100))
    slogan = db.Column(db.String(3000))
    gender = db.Column(db.String(100))
    dateofbirth_user = db.Column(db.DateTime, default=datetime.utcnow)
    twitter = db.Column(db.String(100))
    facebook = db.Column(db.String(100))
    linked_in = db.Column(db.String(100))
    google = db.Column(db.String(100))