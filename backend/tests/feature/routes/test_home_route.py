"""Test the default home route '/'"""

from app import create_app


def test_home_page_get():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that a '200' status code is returned

    """

    # created_app = create_app(test_config=True)
    created_app = create_app()

    with created_app.test_client() as testing_client:
        # Establish an application context
        with created_app.app_context():
            response = testing_client.get('/')
            assert response.status_code == 200
            assert b"Microblog" not in response.data
            assert b"Index Page" in response.data

def test_home_page_post_returns_status_error():
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned

    """

    created_app = create_app()

    with created_app.test_client() as testing_client:
        # Establish an application context
        with created_app.app_context():
            response = testing_client.post('/')
            assert b'"status": "error"' in response.data

def test_home_page_post_returns_status_code_405():
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned

    """

    created_app = create_app()

    with created_app.test_client() as testing_client:
        # Establish an application context
        with created_app.app_context():
            response = testing_client.post('/')
            assert response.status_code == 405


def test_home_page_post_returns_json():
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned

    """

    created_app = create_app()

    with created_app.test_client() as testing_client:
        # Establish an application context
        with created_app.app_context():
            response = testing_client.post('/')
            assert response.json is not None


            