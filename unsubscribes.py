import flask, flask.views
from flask import request
from flask import current_app as app
import db
import pymongo
import filters

from flask.ext.paginate import Pagination

class Unsubscribes(flask.views.MethodView):

	def get(self):
		filters = ['email']
		params = {}
		for arg in request.args:
			val = request.args.get(arg)
			if val:
				params[arg] = val.strip()

		mongo = app.mongo
		unsubscribes = mongo.db.billmonkunsubscribes.find(params).sort('createdAt',pymongo.DESCENDING).limit(50)
		
		#unsubscribes = mongo.db.billmonkunsubscribes.find(params).sort('createdAt',pymongo.DESCENDING).paginate(50, 50, False).items
		#print("debug" + unsubscribes.count)
		

		#WHAT OBJ TYPE AND ARGUMENTS
		#PULLING THE SKIP AND LIMIT
		pagination = Pagination(unsubscribes.count, record_name='unsubscribes')
		return flask.render_template('unsubscribes.html', unsubscribes=unsubscribes, filters = filters, pagination=pagination)
		# return flask.render_template('unsubscribes.html', unsubscribes=unsubscribes, filters = filters)


