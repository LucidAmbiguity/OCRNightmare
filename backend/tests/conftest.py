"""conftest file for my fixtures"""
import pytest

from app import create_app

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
    created_app.config.update({
        'SQLALCHEMY_DATABASE_URI':'sqlite:///:memory:'  # pylint: disable=line-too-long
        })
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

#     
