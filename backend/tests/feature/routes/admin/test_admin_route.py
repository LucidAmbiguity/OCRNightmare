"""Test the default admin route '/admin' """
from tests.helpers import (
    is_response_shape_admin,
   
)
Path = '/admin'
def test_admin_page_get(test_client):
    """
    GIVEN a Flask application
    WHEN the '/admin' page is requested (GET)
    THEN check that a '200' status code is returned

    """

    # created_app = create_app(test_config=True)

    response = test_client.get(Path)
    assert response.status_code == 200

def test_admin_response_shape(test_client):
    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_admin(response.json)