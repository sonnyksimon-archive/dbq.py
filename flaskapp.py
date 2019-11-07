import flask
import dbq

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
        return """<code>
dbq.py<br/>
======<br/>
<br/>
Parameters:<br/>
<br/>
    "connection_string" <br/>
<br/>
    Must be a valid connection string. dbq.py uses SQLAlchemy, so test it on your<br/>
    own machine first and ensure that the webserver can reach the database host.<br/>
<br/>
    "sql_query"<br/>
<br/>
    The query to run on the database.<br/>
<br/>
<hr/>
Usage: dbq.py [OPTIONS]<br/>
<br/>
  This little Python script runs SQL statements on databases from the<br/>
  command-line.<br/>
<br/>
  You must pass in a valid connection string.<br/>
<br/>
  The raw query overrides the file query.<br/>
<br/>
Options:<br/>
  --conn TEXT      Connection string.<br/>
  --file FILENAME  SQL query file.<br/>
  --sql TEXT       Raw query.<br/>
  --help           Show this message and exit.<br/>
</code>
"""
    elif flask.request.method == 'POST':
        try:
            data = flask.request.get_json()
            connection_string = data['connection_string']
            sql_query = data['sql_query']
            results = dbq.run(connection_string, sql_query)
            return results, 200
        except Exception as e:
            print(str(e))
            return flask.jsonify(message='Something\'s wrong with your input.'), 404

if __name__ == '__main__':
    app.run()
