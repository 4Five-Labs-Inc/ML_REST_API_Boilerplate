# loads the required modules
from flask import Blueprint, jsonify, request
# loads the service module
from src.services import Services
# creates a sample blueprint to serve the request
test_api=Blueprint('test_api', __name__)

# defines an GET endpoint
@test_api.route('/check_get', methods=['GET'])
def api_sample_get():
    services = Services()
    return services.check_get()

# defines a POST endpoint
@test_api.route('/check_post', methods=['POST'])
def api_sample_post():
    # handle exceptions
    try:
        # extracts the request body with key name
        name = request.json.get('name', '')
        services = Services()
        message = services.check_post(name)
        # creates a success response payload
        response = jsonify({ 'message': message}), 200
        return (response)
    except Exception as e:
        print(':::: Exception occurred ::::')
        # creates an error response payload
        response = jsonify({}),403
        return (response)