from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Status request successfull')
    return response

@app.route("/metric")
def metric():
    return 'data: {UserCount: 140, UserCountActive: 23}'


@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')

    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
