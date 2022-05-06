from configuration.config import db
from flask_bcrypt import generate_password_hash, check_password_hash


class UserVerification(db.Document):
    email = db.ReferenceField('Admin')
    password = db.ReferenceField('Admin')

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password).encode('utf-8')


class Account(db.Document):
    phone = db.IntField(require=True, unique=True)
    branch_name = db.StringField(required=True, unique=True)
    balance = db.IntField(default=0)
    OpenDate = db.StringField(required=True)


class Admin(db.Document):
    admid = db.IntField(required=True, unique=True)
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    Account_handle = db.ListField(db.IntField(), required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class User(db.Document):
    userid = db.IntField(required=True, unique=True)
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    age = db.IntField(required=True)
    gender = db.StringField(required=True)


