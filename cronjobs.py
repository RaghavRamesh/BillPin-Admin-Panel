import flask, flask.views
from flask import request
from flask import current_app as app
import db
import pymongo
import filters


class Cronjobs(flask.views.MethodView):
	
	def get(self):
		
		filters = ['type','key','completed']
		params = {}
		for arg in request.args:
			val = request.args.get(arg)
			if val:
				val = val.strip()
				params[arg] = val
				try:
					val = int(val)
					if val:
						params[arg] = True
				except:
					pass

		mongo = app.mongo
		jobs = mongo.db.cronjobqueue.find(params).limit(2)#.sort('createdAt',pymongo.DESCENDING)

		return flask.render_template('cronjobs.html', jobs=jobs, filters=filters)
			
