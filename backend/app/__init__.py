"""Main App Entry Point"""
import json
# from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import MethodNotAllowed

from flask import Flask,jsonify
# from .extensions import db,ma,migrate,bcrypt,cors


from config import Config

# from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    """
        Creating the application factory
    """

    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    @app.route('/')
    def index():
        """Base Path"""
        return {'index':'Index Page'}

    @app.errorhandler(MethodNotAllowed)
    def handle_exception_method_not_allowed(e):
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({"status": "error"})
        response.content_type = "application/json"
        return response


    return app
