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