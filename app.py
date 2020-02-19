from __future__ import unicode_literals

import logging
import os

import flask
from flask import Flask, request

import handlers
import utils

app = Flask(__name__, instance_path = os.getcwd())

model = utils.load_model('classifier.joblib')


@app.route('/',methods=['GET','POST'])
def test():
    
    if request.method == "POST":

        received = request.get_json(force = True)

        if not utils.check_keys(received):
            return handlers.invalid_keys()

        data = utils.extract_json(received)

        if data == False:
            return handlers.invalid_values()

        series = utils.json_to_pd(data)

        if type(series) == bool:
            return handlers.invalid_values()

        return flask.make_response(model.predict(series)[0], 200)

    else:
        
        return "Flask app to check if human user or bot"


if __name__ == "__main__":

    logging.basicConfig(level=logging.WARNING, filename="logs.log")
    
    app.run(host="0.0.0.0")

