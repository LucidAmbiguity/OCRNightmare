"""Test App projects '/ocrnightmare/projects' """


# pylint: disable=invalid-name unused-argument

# from app.constants.OCRN import OCRN

# from tests.helpers import (
#     is_response_shape_ocrn,
# )

Path = '/ocrnightmare/projects'
def test_ocrn_project_page_get(test_client):

    response = test_client.get(Path)
    assert response.status_code == 200

def test_ocrn_projects_project_page_get(test_client):

    response = test_client.get(Path)

# def test_ocrn_projects_response_shape(test_client):

#     response = test_client.get(Path)
#     assert response.status_code == 200
#     assert is_response_shape_ocrn(response.json)

# def test_ocrn_projects_response_messages(test_client):

#     response = test_client.get(Path)
#     assert response.status_code == 200
#     assert is_response_shape_ocrn(response.json)

#     assert response.json['messages'][0]['code'] == OCRN.ROOT.code
#     assert response.json['messages'][0]['text'] == OCRN.ROOT.text

#     assert response.json['messages'][1]['code'] == OCRN.Realm.code
#     assert response.json['messages'][1]['text'] == OCRN.Realm.text

# def test_ocrn_projects_response_result_data(test_client):

#     response = test_client.get(Path)
#     assert is_response_shape_ocrn(response.json)

#     assert response.json['result']['data'] ==  {'ocrnightmare': 'ocrnightmare root',}