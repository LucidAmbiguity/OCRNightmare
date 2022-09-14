"""conftest file for my fixtures"""
import pytest

from app import create_app
from app.interfaces.db_interface import DBInterface

# pylint: disable=unused-import
from tests.mocked_models import (
    new_user1,
    user1_creds,
    # new_user2,
)

@pytest.fixture(scope='module')
def app():
    """
    Yields:
        app: An AppContext aware of testing DB

    This is still in Danger Mode.
    """
    created_app = create_app(test_config=True)
    created_app.config.update({
            'TESTING': True,
        })
    # created_app.config.update({
    #     'SQLALCHEMY_DATABASE_URI':'sqlite:///:memory:'  # pylint: disable=line-too-long
    #     })
    # other setup can go here

    yield created_app
  # clean up / reset resources here

@pytest.fixture(scope='module')
def test_client(app): # pylint: disable=redefined-outer-name
    """
    Yields:
        testing_client with app context

    This is still in Danger Mode.
    """

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='module')
def test_client_db(test_client): # pylint: disable=redefined-outer-name
    """
    Yields:
        testing_client with app context
        and an active Fresh empty testing DB

    This is still in Danger Mode.
    """

    db_inter = DBInterface()
    db_inter.create_all()

    yield  test_client # this is where the testing happens!

    db_inter.close_and_drop()

