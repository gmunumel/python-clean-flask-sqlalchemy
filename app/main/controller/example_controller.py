from flask import Blueprint, jsonify
from ..service.example_service import ExampleService

example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/examples', methods=['GET'])
def get_all_examples():
    return jsonify(ExampleService.get_all_examples())