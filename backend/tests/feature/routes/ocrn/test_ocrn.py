"""Test App projects '/ocrnightmare/projects' """

from tests.helpers import (
    is_response_shape_ocrn,
)

Path = '/ocrnightmare'
def test_ocrn_page_get(test_client):

    response = test_client.get(Path)
    assert response.status_code == 200


def test_ocrn_response_shape(test_client):

    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_ocrn(response.json)