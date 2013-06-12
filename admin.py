import flask, flask.views

class Admin(flask.views.MethodView):
	def get(self):
		return flask.render_template('admin.html')

	def post(self):
		pass