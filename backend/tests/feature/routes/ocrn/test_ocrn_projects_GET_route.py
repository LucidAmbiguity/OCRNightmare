"""Test App projects GET '/ocrnightmare/projects' """


# pylint: disable=invalid-name unused-argument

from app.constants.OCRN import OCRN
from app.types.my_types import MockProject,MockCount
from unittest.mock import patch
from tests.helpers import (
    is_response_shape_ocrn_projects,

)

Path = '/ocrnightmare/projects'
p1_pg = MockCount(0)
p1_cust = MockCount(0)
p2_pg = MockCount(7)
p2_cust = MockCount(0)
proj_mock1 = MockProject(1,'project001',0,'project001.pdf',p1_pg,p1_cust)
proj_mock2 = MockProject(2,'project002',1,'project002.pdf',p2_pg,p2_cust)

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_page_get(a, test_client):

    response = test_client.get(Path)
    assert response.status_code == 200

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_response_shape(a, test_client):

    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_ocrn_projects(response.json)

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_response_messages(a, test_client):

    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_ocrn_projects(response.json)

    assert response.json['messages'][0]['code'] == OCRN.Projects.code
    assert response.json['messages'][0]['text'] == OCRN.Projects.text

    assert response.json['messages'][1]['code'] == OCRN.Realm.code
    assert response.json['messages'][1]['text'] == OCRN.Realm.text

@patch('app.interfaces.db_project_if.DBProjI.get_all', return_value = [proj_mock1,proj_mock2])
def test_ocrn_projects_response_result_data(a, test_client):

    response = test_client.get(Path)
    assert is_response_shape_ocrn_projects(response.json)

    assert response.json['result']['projects'] ==  [
        {
            'customers': 0,
            'filename': 'project001.pdf',
            'id': 1,
            'name': 'project001',
            'pages': 0,
            'status': 0
        },
        {
            'customers': 0,
            'filename': 'project002.pdf',
            'id': 2,
            'name': 'project002',
            'pages': 7,
            'status': 1
        }
    ]


