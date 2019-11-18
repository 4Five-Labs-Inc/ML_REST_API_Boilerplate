from flask import Flask, jsonify, request, render_template, abort
from src.api import test_api
from jinja2 import TemplateNotFound
application = Flask(__name__ , template_folder='./src/templates')
application.register_blueprint(test_api, url_prefix='/api')

# Loading home page
@application.route('/', defaults={'page': 'index'})
@application.route('/<page>')

# Renders the page
def show(page):
    try:
        return render_template(page+'.html', app_name='ML_REST_API_Boilerplate')
    except TemplateNotFound:
        abort(404)

# Handling 400 Error
@application.errorhandler(400)
def bad_request(error=None):
    # constructs the response payload
    message = {
        'status': 400,
        'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
    }
    resp = jsonify(message), 400
    return resp

# run application
if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')