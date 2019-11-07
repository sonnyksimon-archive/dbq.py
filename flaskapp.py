import flask
import dbq

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
        resp = flask.Response(flask.render_template('doc.txt'))
        resp.headers['content-type'] = 'text/plain'
        return resp
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
