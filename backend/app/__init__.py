"""Main App Entry Point"""
import json
# from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import MethodNotAllowed,HTTPException

from flask import Flask,jsonify
# from .extensions import db,ma,migrate,bcrypt,cors


from config import Config

# from flask_cors import CORS, cross_origin


def create_app():
    """the app factory"""
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    app.config.from_object(Config)

    # # Register the blueprints
    from .auth import auth # pylint:disable=import-outside-toplevel
    app.register_blueprint(auth, url_prefix='/auth')

    @app.route('/')
    def index():
        """Base Path"""
        return {'index':'Index Page'}

    @app.errorhandler(HTTPException)
    def handle_exception_http_exception(err):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = err.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            'status': 'error',
            'code': err.code,
            'messages' : [{
                    'code': err.code,
                    'text': err.name,
                  }],
            'result': {'description': err.description}
        })
        response.content_type = 'application/json'
        return response

    @app.errorhandler(MethodNotAllowed)
    def handle_exception_method_not_allowed(err):
        """Return JSON instead of HTML for HTTP errors."""
        print('handle_exception_method_not_allowed')
        # start with the correct headers and status code from the error
        response = err.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            'status': 'error',
            'code': err.code,
            'messages' : [{
                    'code': err.code,
                    'text': err.name,
                  }],
            'result': {'description': err.description}
        })
        response.content_type = 'application/json'
        return response

    return app
