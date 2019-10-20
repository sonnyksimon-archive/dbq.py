import flask
import dbq

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'POST':
        try:
            data = flask.request.get_json()
            connection_string = data['connection_string']
            sql_query = data['sql_query']
            results = dbq.run(connection_string, sql_query)
            return flask.jsonify(results), 200
        except:
            return flask.jsonify(message='Something\'s wrong with your input.'), 404
    return """<code>
dbq.py
======

Parameters:

    "connection_string" 

    Must be a valid connection string. dbq.py uses SQLAlchemy, so test it on your
    own machine first and ensure that the webserver can reach the database host.

    "sql_query"

    The query to run on the database.
</code>
"""
