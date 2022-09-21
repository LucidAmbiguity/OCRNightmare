"""Test App projects POST '/ocrnightmare/projects' """
# pylint: disable=invalid-name unused-argument



from app.constants.OCRN import OCRN
from app.constants.other import PDF

# from app.types.my_types import MockProject,MockCount
# from unittest.mock import patch
from tests.helpers import (
    # is_response_shape_ocrn_one_project,
    is_response_shape_ocrn_error,
)

Path = '/ocrnightmare/projects'




def test_ocrn_projects_page_post_fails_if_no_form_data( test_client):

    response = test_client.post(Path)
    assert response.status_code == 400


def test_ocrn_projects_page_post_fails_if_bad_form_data(Data_w_FileBad_CRF, test_client):
    """ Example using real file and context """

    response = test_client.post(Path, data=Data_w_FileBad_CRF)

    assert response.status_code == 400


def test_ocrn_projects_page_post_fails_if_bad_form_data2(Data_w_FileBad, test_client):
    """ Example using fake file no context
    """
    response = test_client.post(Path, data=Data_w_FileBad ,)

    assert response.status_code == 400


def test_ocrn_projects_page_post_fails_response_shape(Data_w_FileBad, test_client): #for good form

    response = test_client.post(Path, data=Data_w_FileBad ,)

    assert is_response_shape_ocrn_error(response.json)


def test_ocrn_projects_page_post_FAILinForm_response_messages(Data_w_FileBad, test_client):

    response = test_client.post(Path, data=Data_w_FileBad)

    assert response.status_code == 400

    assert response.json['messages'][0]['code'] == OCRN.FAILinForm.code
    assert response.json['messages'][0]['text'] == OCRN.FAILinForm.text

    assert response.json['messages'][1]['code'] == OCRN.Realm.code
    assert response.json['messages'][1]['text'] == OCRN.Realm.text



# def test_ocrn_projects_page_post_FAILinDir_response_messages(Data_w_FileBad, test_client):

#     response = test_client.post(Path, data=Data_w_FileBad)

#     assert response.status_code == 400

#     assert response.json['messages'][0]['code'] == OCRN.FAILinForm.code
#     assert response.json['messages'][0]['text'] == OCRN.FAILinForm.text

#     assert response.json['messages'][1]['code'] == OCRN.Realm.code
#     assert response.json['messages'][1]['text'] == OCRN.Realm.text




# def test_ocrn_projects_response_result_data(a, test_client):
    # project_name = Data_w_FileBad['upfile'][1][:PDF]

#     response = test_client.post(Path)
#     assert is_response_shape_ocrn_projects(response.json)

#     assert response.json['result']['projects'] ==  [
#         {
#             'customers': 0,
#             'filename': 'project001.pdf',
#             'id': 1,
#             'name': 'project001',
#             'pages': 0,
#             'status': 0
#         },
#         {
#             'customers': 0,
#             'filename': 'project002.pdf',
#             'id': 2,
#             'name': 'project002',
#             'pages': 7,
#             'status': 1
#         }
#     ]


