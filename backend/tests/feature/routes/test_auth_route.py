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
    WHEN the '/' page is requested to (GET)
    THEN check that a json is returned

    """

    response = test_client.post('/auth')
    assert response.json is not None

def test_auth_page_get_response_shape(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is posted to (GET)
    THEN check shape of returned response

    """

    response = test_client.get('/auth')
    

    assert 'code' in response.json.keys()
    assert 'messages' in response.json.keys()
    assert 'result' in response.json.keys()
    assert 'status' in response.json.keys()
    
    assert 'code' in response.json['messages'][0].keys()
    assert 'text' in response.json['messages'][0].keys()

    assert 'links' in response.json['result'].keys()

    assert 'login' in response.json['result']['links'].keys()
    assert 'register' in response.json['result']['links'].keys()



