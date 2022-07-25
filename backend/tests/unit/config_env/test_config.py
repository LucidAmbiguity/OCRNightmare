"""test"""
from config import Config
from app import create_app

def test_config_class_exists_and_has_expected_attributes():
    """
    Test config.py Exists and has expected Attributes
    basic Attributes needed by a simple flask app
    Getting this to a state similar to that created by
    create-react-app for react.
        basic config and setup for a Flask Factory app
        with DB
    """
    assert hasattr(Config,'FLASK_APP')
    assert hasattr(Config,'SECRET_KEY')
    assert hasattr(Config,'SQLALCHEMY_DATABASE_URI')
    assert hasattr(Config,'SQLALCHEMY_TRACK_MODIFICATIONS')
  # ['FLASK_APP', 'SECRET_KEY', 'SQLALCHEMY_DATABASE_URI', 'SQLALCHEMY_TRACK_MODIFICATIONS']



