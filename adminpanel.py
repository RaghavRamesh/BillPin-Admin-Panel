import flask, flask.views
import settings
import db
import pymongo
from flask.ext.pymongo import PyMongo

from flask import current_app as app

# Views
from admin import Admin
from users import Users 
from usertransactions import UserTransactions
from cronjobs import Cronjobs
from emails import Emails
from unsubscribes import Unsubscribes


app = flask.Flask(__name__)


# Config Mongo
mongo = db.establish_mongo_connection(app)
app.mongo = mongo

# Config secret key
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/adminnew',
				view_func=Admin.as_view('admin'),
				methods=["GET", "POST"])
app.add_url_rule('/adminnew/users',
				view_func=Users.as_view('users'),
				methods=["GET", "POST"])
app.add_url_rule('/adminnew/transactions',
				view_func=UserTransactions.as_view('transactions'),
				methods=["GET"])
app.add_url_rule('/adminnew/cronjobs',
				view_func=Cronjobs.as_view('cronjobs'),
				methods=["GET"])
app.add_url_rule('/adminnew/emails',
				view_func=Emails.as_view('emails'),
				methods=["GET"])
app.add_url_rule('/adminnew/unsubscribes',
				view_func=Unsubscribes.as_view('unsubscribes'),
				methods=["GET"])



# Run app in debug mode
app.run(debug = 'TRUE')
