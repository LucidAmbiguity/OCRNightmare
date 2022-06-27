"""test"""
from config import Config

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

# def test_config_class_exists_and_where():
#     """
#     Test config class exists and where

#     In a perfect world this test will be commented out
#     it purpose is to find where config is loading from
#     as !existence will throw [ModuleNotFoundError: No module named 'config']
#     however a stray bad path in your sys.path may cause files to import from the void.

#     if you suspect such a thing uncomment this test 
#         it will fail forcing output of the print to show where
#         in the void it came from
#     """

#     import config # pylint:disable=import-outside-toplevel
#     print(config.__file__)
#     assert False
