import flask, flask.views
from parseDB import Parse
from flask import request

class UserTransactions(flask.views.MethodView):
	

	def get(self):
		parse = Parse()
		transactions = parse.getActivitiesRecursive(0, 10)

		searchString = request.args.get('search')
		txns = parse.getEventsWithUserWrapper(searchString)
		print(txns)
		
		return flask.render_template('transactions.html', transactions = transactions, txns = txns)