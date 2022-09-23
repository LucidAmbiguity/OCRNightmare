"""Test App projects '/ocrnightmare/projects/extract' """

# pylint: disable=invalid-name unused-argument

from unittest.mock import patch
from app.constants.OCRN import OCRN
from app.types.my_types import MockProject,MockCount
from app.constants.other import PDF
from app.types.my_types import ProjDataT


from tests.helpers import (
    is_response_shape_ocrn_one_project,
    is_response_shape_ocrn_error
)


def Path(proj_name:str)->str:
    return f'/ocrnightmare/projects/{proj_name}/extract'

PDF_TestFile_Name_Good = 'test_input.pdf'
PDF_TestFile_Name_Bad = 'test_input.jpg'
BAD_ProjName = 'doesnotexist'

proj_data_mock_1 = ProjDataT(
        id = 1,
        name = PDF_TestFile_Name_Good[:PDF],
        status = 1,
        filename = PDF_TestFile_Name_Good,
        pages = 7,
        customers = 0,
    )

p1_pg = MockCount(0)
p1_cust = MockCount(0)
proj_mock1 = MockProject(1,PDF_TestFile_Name_Good[:PDF],0,PDF_TestFile_Name_Good,p1_pg,p1_cust)
# @patch('app.services.extraction_s.extraction_s', return_value = proj_mock1)


def test_extract_page_get(test_client):
    response = test_client.get(Path(proj_mock1.name))

    assert response.status_code == 405
    assert is_response_shape_ocrn_error(response.json)

@patch('app.routes.ocrnightmare.bp.extract.extract.extraction_s', return_value = None)
def test_extract_page_post_doesnotexist(a,test_client):

    response = test_client.post(Path(BAD_ProjName))

    assert response.status_code == 404
    assert is_response_shape_ocrn_error(response.json)


@patch('app.routes.ocrnightmare.bp.extract.extract.extraction_s', return_value = proj_data_mock_1)
def test_extract_page_post(a,test_client):

    response = test_client.post(Path(proj_mock1.name))

    assert response.status_code == 200
    assert is_response_shape_ocrn_one_project(response.json)


    assert response.json['messages'][0]['code'] == OCRN.Extract.ROOT.code
    assert response.json['messages'][0]['text'] == OCRN.Extract.ROOT.text

    assert response.json['messages'][1]['code'] == OCRN.Realm.code
    assert response.json['messages'][1]['text'] == OCRN.Realm.text
    assert response.json['result']['project']   == {
            'customers': proj_data_mock_1['customers'],
            'filename': proj_data_mock_1['filename'],
            'id': proj_data_mock_1['id'],
            'name': proj_data_mock_1['name'],
            'pages': proj_data_mock_1['pages'],
            'status': proj_data_mock_1['status'],
        }

