""" Fixtures for features.routes.ocrn"""
# pylint: disable=invalid-name unused-argument


import pytest
import io

PDF_TestFile = 'tests/feature/routes/ocrn/test_input.pdf'
PDF_TestFile_Name_Bad = 'test_input.jpg'
PDF_TestFile_Name_Good = 'test_input.pdf'
File_FormFieldName = 'upfile'


@pytest.fixture(scope='function')
def Data_w_FileBad():  # pylint: disable=unused-argument
    return  {File_FormFieldName: (io.BytesIO(b'abcdef'), PDF_TestFile_Name_Bad)}

@pytest.fixture(scope='function')
def Data_w_FileGood():  # pylint: disable=unused-argument
    return  {File_FormFieldName: (io.BytesIO(b'abcdef'), PDF_TestFile_Name_Good)}

@pytest.fixture(scope='function')
def Data_w_FileBad_CRF():  # pylint: disable=unused-argument
    """ Yield context with real test file """

    with open(PDF_TestFile, 'rb') as ptf :
        data = {File_FormFieldName: (ptf, PDF_TestFile_Name_Bad)}
        yield data

@pytest.fixture(scope='function')
def Data_w_FileGood_CRF():  # pylint: disable=unused-argument
    """ Yield context with real test file """

    with open(PDF_TestFile, 'rb') as ptf :
        data = {File_FormFieldName: (ptf, PDF_TestFile_Name_Good)}
        yield data

