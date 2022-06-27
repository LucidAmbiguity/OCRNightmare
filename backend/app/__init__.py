
import json
# from werkzeug.exceptions import HTTPException
from flask import Flask
# from .extensions import db,ma,migrate,bcrypt,cors


from config import Config

# from flask_cors import CORS, cross_origin

# Creating the application factory
def create_app(test_config=None):
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    @app.route('/')
    def index():
        return {'index':'Index Page'}


    return app