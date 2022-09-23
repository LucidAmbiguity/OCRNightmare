"""Test App projects GET '/ocrnightmare/projects/<proj_name>' """


# pylint: disable=invalid-name unused-argument

from app.constants.OCRN import OCRN
from app.types.my_types import MockProject,MockCount
from unittest.mock import patch
from tests.helpers import (
    is_response_shape_ocrn_one_project,
    is_response_shape_ocrn_error

)

def Path(proj_name:str)->str:
    return f'/ocrnightmare/projects/{proj_name}'
p1_pg = MockCount(0)
p1_cust = MockCount(0)
proj_mock1 = MockProject(1,'project001',0,'project001.pdf',p1_pg,p1_cust)
# p2_pg = MockCount(7)
# p2_cust = MockCount(0)
# proj_mock2 = MockProject(2,'project002',1,'project002.pdf',p2_pg,p2_cust)

@patch('app.repositories.projects_repo.DBProjI.get_by_name', return_value = proj_mock1)
def test_ocrn_projects_projname_get_SUCCESS_return_shape_and_codes_messages(a, test_client):

    response = test_client.get(Path(proj_mock1.name))
    print(response.json)

    assert response.status_code == 200
    assert is_response_shape_ocrn_one_project(response.json)


    assert response.json['messages'][0]['code'] == OCRN.Project_.code
    assert response.json['messages'][0]['text'] == OCRN.Project_.text(proj_mock1.name)

    assert response.json['messages'][1]['code'] == OCRN.Realm.code
    assert response.json['messages'][1]['text'] == OCRN.Realm.text
    assert response.json['result']['project']   == {
            'customers': proj_mock1.customers.count(),
            'filename': proj_mock1.filename,
            'id': proj_mock1.id,
            'name': proj_mock1.name,
            'pages': proj_mock1.pages.count(),
            'status': proj_mock1.status,
        }

@patch('app.repositories.projects_repo.DBProjI.get_by_name', return_value = None)
def test_ocrn_projects_projname_get_Fail(a, test_client):

    response = test_client.get(Path(proj_mock1.name))
    print(response.json)

    assert response.status_code == 404
    assert is_response_shape_ocrn_error(response.json)



