"""Test the default auth route '/auth'"""


def test_auth_page_get(test_client):
    """
    GIVEN a Flask application
    WHEN the '/auth' page is requested (GET)
    THEN check that a '200' status code is returned

    """

    # created_app = create_app(test_config=True)

    response = test_client.get('/auth')
    assert response.status_code == 200


def test_auth_page_get_returns_json(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (GET)
    THEN check that a '405' status code is returned

    """

    response = test_client.post('/')
    assert response.json is not None
