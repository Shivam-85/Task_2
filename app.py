from flask import Flask
from flask_restful import Api
from configuration.config import initialize_db, initialize_mail
from flask_bcrypt import Bcrypt
from urls.errors import *
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USERNAME'] = 'support@bank.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['DEBUG'] = True
mail = Mail(app)

from urls.url import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/bank_Management'
}
initialize_mail(app)
initialize_db(app)
initialize_routes(api)

