"""Test App projects '/ocrnightmare/projects' """


# pylint: disable=invalid-name unused-argument

# from app.constants.OCRN import OCRN
from app.types.my_types import ProjDataT
from unittest.mock import patch
from tests.helpers import (
    is_response_shape_ocrn_projects,

)

Path = '/ocrnightmare/projects'

proj_mock1 = ProjDataT(1,'project001',0,'project001.pdf')
proj_mock2 = ProjDataT(2,'project002',1,'project002.pdf')

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_page_get(a, test_client):

    response = test_client.get(Path)
    assert response.status_code == 200

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_response_shape(a, test_client):

    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_ocrn_projects(response.json)

# def test_ocrn_projects_response_messages(test_client):

#     response = test_client.get(Path)
#     assert response.status_code == 200
#     assert is_response_shape_ocrn_projects(response.json)

#     assert response.json['messages'][0]['code'] == OCRN.ROOT.code
#     assert response.json['messages'][0]['text'] == OCRN.ROOT.text

#     assert response.json['messages'][1]['code'] == OCRN.Realm.code
#     assert response.json['messages'][1]['text'] == OCRN.Realm.text

# def test_ocrn_projects_response_result_data(test_client):

#     response = test_client.get(Path)
#     assert is_response_shape_ocrn_projects(response.json)

#     assert response.json['result']['data'] ==  {'ocrnightmare': 'ocrnightmare root',}
