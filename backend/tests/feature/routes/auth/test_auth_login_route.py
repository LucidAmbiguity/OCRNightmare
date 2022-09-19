"""Test the auth register route '/auth/login'"""

# pylint: disable=invalid-name unused-argument

from app.types.my_types import MockUser
from unittest.mock import patch
from werkzeug.security import generate_password_hash

from base64 import b64encode
# from tests.helpers import is_response_shape_success
from tests.helpers import is_response_shape_auth_error
Path = '/auth/login'



def test_auth_login_page_GET_returns_405(test_client):

    response = test_client.get(Path)

    assert response.status_code == 405


def test_auth_login_page_post_response_shape(test_client):

    response = test_client.post(Path)

    assert  response.status_code == 401
    assert  is_response_shape_auth_error(response.json) is True

def test_auth_login_page_headers_contains_basic_auth_info_for_missing_auth_info(test_client):

    credentials_nu = b64encode(b':barkbark').decode('utf-8')
    credentials_np = b64encode(b'TEST1:').decode('utf-8')

    response_no_user = test_client.post(Path, headers={'Authorization': f'Basic {credentials_nu}'})
    response_no_pass = test_client.post(Path, headers={'Authorization': f'Basic {credentials_np}'})

    assert  is_response_shape_auth_error(response_no_user.json) is True
    assert  is_response_shape_auth_error(response_no_pass.json) is True

    assert response_no_user.json['messages'][0]['code'] == 'AL0012'
    assert response_no_user.json['messages'][0]['text'] == 'Username and Password Required'

    assert response_no_pass.json['messages'][0]['code'] == 'AL0012'
    assert response_no_pass.json['messages'][0]['text'] == 'Username and Password Required'

    assert response_no_user.json['messages'][1]['code'] == 'AR0003'
    assert response_no_user.json['messages'][1]['text'] == "Basic realm: 'login required'"

    assert response_no_pass.json['messages'][1]['code'] == 'AR0003'
    assert response_no_pass.json['messages'][1]['text'] == "Basic realm: 'login required'"



@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = None)
def test_auth_login_bad_username_fails(a,test_client):

    username = 'TEST1'
    password = 'bark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')


    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert response.json['messages'][0]['code'] == 'AL0015'
    assert response.json['messages'][0]['text'] == f'Login Failed for {username} : Bad username or password'


user_mock = MockUser('pub_id','name','mockpassword',False)
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = user_mock)
def test_auth_login_bad_password_fails(a,test_client):

    username = 'TEST1'
    password = 'bark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')


    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert response.json['messages'][0]['code'] == 'AL0015'
    assert response.json['messages'][0]['text'] == f'Login Failed for {username} : Bad username or password'


mock_pass = 'password'
mock_pass_hash = generate_password_hash(mock_pass, method='sha256')
user_mock = MockUser('pub_id','name',mock_pass_hash,False)
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_username', return_value = user_mock)
def test_auth_login_good_creds_pass(a,test_client):

    username = 'TEST1'
    password = mock_pass
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')


    response = test_client.post(Path, headers={'Authorization': f'Basic {credentials}'})

    assert response.json['messages'][0]['code'] == 'AL0020'
    assert response.json['messages'][0]['text'] == 'Login Successful'

    assert response.json['result']['login'] == 'Success'
    assert response.json['result']['public_id'] == 'pub_id'
    cookie = next(
        (cookie for cookie in test_client.cookie_jar if cookie.name == "token"),
        None
    )
    assert cookie is not None



