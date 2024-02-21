""" APP Initialization File """
from flask import (
    Flask
)
from flask_cors import CORS
from libs.logger import create_logger
from flask_restx import Api
from .apis import (
    common
)

app = Flask(__name__)
api = Api(
    app,
    title="Logstash Flask Test",
    version="1.0",
    prefix="/api",
    doc="/api/swagger",
)

app_logger = create_logger("logstash-flask-test")
app.logger = app_logger

CORS(app, supports_credentials=True)

api.add_namespace(common.api, path="/common")