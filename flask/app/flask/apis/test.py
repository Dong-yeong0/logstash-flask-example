"""Define APIs for test"""
from flask import jsonify
from flask_restx import Resource, Namespace

api = Namespace(
    name="Common",
)


@api.route("")
class Test(Resource):
    def get(self):
        return jsonify("Hello world!")

