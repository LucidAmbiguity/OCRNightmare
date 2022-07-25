"""conftest file for my fixtures"""
import pytest

from app import create_app

@pytest.fixture(scope='module')
def app():
    """
    Yields:
        app: An AppContext
    """
    created_app = create_app()
    yield created_app

@pytest.fixture(scope='module')
def test_client(app): # pylint: disable=redefined-outer-name
    """
    Yields:
        testing_client with app context
    """
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!
