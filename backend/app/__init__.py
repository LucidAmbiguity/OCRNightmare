#type: ignore[misc]
"""Main App Entry Point"""
import json
# from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import MethodNotAllowed,HTTPException

from flask import Flask,jsonify

from app.constants.OCRN import OCRN
# from .extensions import db,ma,migrate,bcrypt,cors
from .extensions import db, ma, migrate, bcrypt, cors

from config import Config
from typing import TYPE_CHECKING
# from flask_cors import CORS, cross_origin
if TYPE_CHECKING:
    from flask import Response

def create_app(test_config: str=None) -> Flask:
    """the app factory"""
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        from config import TestConfig  # pylint: disable=import-outside-toplevel
        app.config.from_object(TestConfig)

    # # Initialization of extension instances
    db.init_app(app) # type: ignore[misc]
    ma.init_app(app) # type: ignore[misc]
    migrate.init_app(app, db) # type: ignore[misc]
    bcrypt.init_app(app) # type: ignore[misc]
    cors.init_app(app, supports_credentials=True) # type: ignore[misc]


    # # Register the blueprints
    from .routes.auth import auth # pylint:disable=import-outside-toplevel
    app.register_blueprint(auth, url_prefix='/auth')
    from .routes.admin import admin # pylint:disable=import-outside-toplevel
    app.register_blueprint(admin, url_prefix='/admin')
    from .routes.ocrnightmare import ocrnightmare # pylint:disable=import-outside-toplevel
    app.register_blueprint(ocrnightmare, url_prefix='/ocrnightmare')




    @app.route('/') #type: ignore[misc]
    def index()->'Response':
        """Base Path"""
        return {'index':'Index Page'} # type: ignore[return-value]

    @app.errorhandler(HTTPException) #type: ignore[misc]
    def handle_exception_http_exception(err)->'Response':
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
                  },
                  {
                    'code': OCRN.Realm.code,
                    'text': OCRN.Realm.text,
                  }],
            'result': {'description': err.description,
                       'errors':{
                            'code': err.code,
                            'text': err.name,
                        }
            }
        })
        response.content_type = 'application/json'
        return response


    @app.errorhandler(MethodNotAllowed) #type: ignore[misc]
    def handle_exception_method_not_allowed(err)->'Response':
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
                  },
                  {
                    'code': OCRN.Realm.code,
                    'text': OCRN.Realm.text,
                  }],
            'result': {'description': err.description,
                       'errors':{
                            'code': err.code,
                            'text': err.name,
                        }
            }
        })
        response.content_type = 'application/json'
        return response

    return app
