import flask, flask.views
from parseDB import Parse
from flask import request
from flask import current_app as app
import db
import pymongo
import filters


class Emails(flask.views.MethodView):

	def get(self):
		filters = ['type','to']	
		params = {}

		for arg in request.args:
			val = request.args.get(arg)
			if val:
				params[arg] = val.strip()

		mongo = app.mongo
		emailanalytics = mongo.db.emailanalytics.find(params).sort('sentAt', pymongo.DESCENDING).limit(2)
		
		return flask.render_template('emails.html', emailanalytics=emailanalytics, filters=filters)

