""" APP Initialization File """
from flask import (
    Flask
)
from flask_cors import CORS
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from packages.logger import create_logger
from flask_restx import Api
from apis import (
    test,
)

app = Flask(__name__)
api = Api(
    app,
    title="Logstash Flask Test",
    version="2.0",
    prefix="/api/test",
    doc="/api/test",
)

app_logger = create_logger("logstash-flask-test")
app.logger = app_logger

CORS(app, supports_credentials=True)

api.add_namespace(test.api, path="/")

app.run(debug=True)