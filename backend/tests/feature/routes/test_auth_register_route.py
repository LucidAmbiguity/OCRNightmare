"""Test the auth register route '/auth/register'"""

# pylint: disable=invalid-name

from base64 import b64encode
from unittest.mock import patch

from tests.helpers import is_response_shape_success
from tests.helpers import is_response_shape_error
Path = '/auth/register'



def test_auth_register_page_GET_returns_405(test_client):

    response = test_client.get(Path)

    assert response.status_code == 405


def test_auth_register_page_GET_returns_json(test_client):

    response = test_client.get(Path)

    assert response.json is not None


def test_auth_register_page_post_response_shape(test_client):


    response = test_client.post(Path)
    assert  response.status_code == 401
    assert  is_response_shape_error(response.json) is True


def test_auth_register_page_headers_contains_basic_auth_info_for_missing_auth_info(test_client):

    credentials_nu = b64encode(b':barkbark').decode('utf-8')
    credentials_np = b64encode(b'TEST1:').decode('utf-8')

    response_no_user = test_client.post(Path, headers={'Authorization': f'Basic {credentials_nu}'})
    response_no_pass = test_client.post(Path, headers={'Authorization': f'Basic {credentials_np}'})

    assert  is_response_shape_error(response_no_user.json) is True
    assert  is_response_shape_error(response_no_pass.json) is True

    assert response_no_user.json['messages'][0]['code'] == 'AR0002'
    assert response_no_user.json['messages'][0]['text'] == 'Username and Password Required'

    assert response_no_pass.json['messages'][0]['code'] == 'AR0002'
    assert response_no_pass.json['messages'][0]['text'] == 'Username and Password Required'

    assert response_no_user.json['messages'][1]['code'] == 'AR0003'
    assert response_no_user.json['messages'][1]['text'] == "Basic realm: 'login required'"

    assert response_no_pass.json['messages'][1]['code'] == 'AR0003'
    assert response_no_pass.json['messages'][1]['text'] == "Basic realm: 'login required'"


def test_username_less_than_3_is_error(test_client):

    username = 'TE'
    password = 'barkbark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')

    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert is_response_shape_error(response.json) is True
    assert response.json['messages'][0]['code'] == 'AR0004'
    assert response.json['messages'][0]['text'] == f'{username} is to short. At Least 3 characters please'

    assert response.json['messages'][1]['code'] == 'AR0003'
    assert response.json['messages'][1]['text'] == "Basic realm: 'login required'"


@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = 'not None')
def test_existing_username_fails_to_register(my_mock,test_client,user1_creds):

    response = test_client.post(Path, headers={'Authorization': f'Basic {user1_creds[0]}'})
    # print('test_existing_username_fails_to_register',response.json)
    # print(user1_creds)
    assert is_response_shape_error(response.json) is True
    assert response.json['messages'][0]['code'] == 'AR0005'
    assert response.json['messages'][0]['text'] == f'{user1_creds[1]} Is in use'

    assert response.json['messages'][1]['code'] == 'AR0003'
    assert response.json['messages'][1]['text'] == "Basic realm: 'login required'"


@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = None)
def test_short_password_fails_to_register(my_mock,test_client):

    username = 'TEST1'
    password = 'bark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')

    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})
    # print('test_existing_username_fails_to_register',response.json)
    # print(user1_creds)
    assert is_response_shape_error(response.json) is True
    assert response.json['messages'][0]['code'] == 'AR0006'
    assert response.json['messages'][0]['text'] == 'Password  is to short. At Least 8 characters please'

    assert response.json['messages'][1]['code'] == 'AR0003'
    assert response.json['messages'][1]['text'] == "Basic realm: 'login required'"



@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = None)
@patch('app.interfaces.db_user_if.DBUserI.new_user', return_value = None)
def test_valid_creds_fail_in_db_creation_unknown_failure(a,b,test_client):

    username = 'TEST1'
    password = 'barkbark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')

    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert is_response_shape_error(response.json) is True
    assert response.json['messages'][0]['code'] == 'AR0007'
    assert response.json['messages'][0]['text'] == 'creation error'

    assert response.json['messages'][1]['code'] == 'AR0003'
    assert response.json['messages'][1]['text'] == "Basic realm: 'login required'"




@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = None)
@patch('app.interfaces.db_user_if.DBUserI.new_user', return_value = {'public_id':'pubid'})
def test_valid_creds_do_register(a,b,test_client):

    username = 'TEST1'
    password = 'barkbark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')

    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert is_response_shape_success(response.json) is True
    assert response.json['messages'][0]['code'] == 'AR0010'
    assert response.json['messages'][0]['text'] == 'Register Successful'
    assert response.json['result']['public_id'] == 'pubid'





