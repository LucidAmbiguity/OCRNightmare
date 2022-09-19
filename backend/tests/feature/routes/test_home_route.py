"""Test the default home route '/'"""

# pylint: disable=invalid-name unused-argument

def test_home_page_get(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that a '200' status code is returned

    """

    # created_app = create_app(test_config=True)

    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_home_page_post_returns_status_error(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a :: '"status": "error"'

    """

    response = test_client.post('/')
    assert b'"status": "error"' in response.data

def test_home_page_post_returns_status_code_405(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a '405' status code is returned

    """
    response = test_client.post('/')
    assert response.status_code == 405


def test_home_page_post_returns_json(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (POST)
    THEN check that a json response is returned

    """

    response = test_client.post('/')
    assert response.json is not None

def test_home_page_get_returns_json(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested to (GET)
    THEN check that a json response is returned

    """

    response = test_client.get('/')
    assert response.json is not None
