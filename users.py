import flask, flask.views
from parseDB import Parse
from flask import request

from flask.ext.paginate import Pagination

class Users(flask.views.MethodView):
	

	def get(self):	
		parse = Parse()
		# fetches users
		users = parse.getUserWrappersWithUserRecursive(0, 10)
		
		# search by objectId
		searchString = request.args.get('search')
		userWrapper = parse.getUserWrapperWithObjectId(searchString)
		
		# update
		objectId = request.args.get('update')
		update(objectId)
		return flask.render_template('users.html', users = users, userWrapper = userWrapper)


	def update(self, objectId):
		pass
	
