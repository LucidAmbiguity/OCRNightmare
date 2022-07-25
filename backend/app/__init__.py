"""Main App Entry Point"""
import json
# from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import MethodNotAllowed,HTTPException

from flask import Flask,jsonify
# from .extensions import db,ma,migrate,bcrypt,cors


from config import Config

# from flask_cors import CORS, cross_origin


def create_app():
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    
    
    app.config.from_object(Config)
    
    @app.route('/')
    def index():
        """Base Path"""
        return {'index':'Index Page'}

    

    @app.route("/auth/", methods=['GET', 'POST'])
    @app.route("/auth", methods=['GET', 'POST'])
    def auth_root():
        """Root route of App Module"""
        return {'auth':'auth root'}

   
    @app.errorhandler(HTTPException)
    def handle_exception_http_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "status": "error",
            "code": e.code,
            "messages" : [{
                    "code": e.code,
                    "text": e.name,
                  }],
            "result": {"description": e.description}
        })
        response.content_type = "application/json"
        return response
  
    @app.errorhandler(MethodNotAllowed)
    def handle_exception_method_not_allowed(e):
        """Return JSON instead of HTML for HTTP errors."""
        print("handle_exception_method_not_allowed")
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "status": "error",
            "code": e.code,
            "messages" : [{
                    "code": e.code,
                    "text": e.name,
                  }],
            "result": {"description": e.description}
        })
        response.content_type = "application/json"
        return response
  
    return app






