from .db import db


class User(db.Document):
    name = db.StringField(required=True, unique=True)
    phone = db.StringField(required=True, unique=True)
    age = db.IntField(required=True)
    gender = db.StringField(required=True)

