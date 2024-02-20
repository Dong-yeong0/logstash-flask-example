"""Define APIs for test"""
from flask import jsonify, current_app
from flask_restx import Resource, Namespace

api = Namespace(
    name="Common",
)


@api.route("")
class Test(Resource):
    def get(self):
        current_app.logger.info("Test")
        return jsonify("Hello world!")

