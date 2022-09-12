"""Test the auth register route '/auth/register'"""

# pylint: disable=invalid-name

from base64 import b64encode


Path = '/auth/register'

def is_response_shape(res_object):
    return all([
         'code' in res_object.keys(),
         'messages' in res_object.keys(),
         'result' in res_object.keys(),
         'status' in res_object.keys(),

         'code' in res_object['messages'][0].keys(),
         'text' in res_object['messages'][0].keys(),
         'code' in res_object['messages'][1].keys(),
         'text' in res_object['messages'][1].keys(),

         'links' in res_object['result'].keys(),

         'login' in res_object['result']['links'].keys(),
         'register' in res_object['result']['links'].keys(),

    ])


def test_auth_register_page_GET_returns_405(test_client):

    response = test_client.get(Path)

    assert response.status_code == 405


def test_auth_register_page_GET_returns_json(test_client):

    response = test_client.get(Path)

    assert response.json is not None


def test_auth_register_page_post_response_shape(test_client):


    response = test_client.post(Path)

    assert  is_response_shape(response.json) is True

    
def test_auth_register_page_headers_contains_basic_auth_info_for_missing_auth_info(test_client):
 
    password = 'barkbark'
    username = 'Rufus'

    response_none = test_client.post(Path)
    response_no_user = test_client.post(Path, headers={'Authorization': f'Basic {username}:'})
    response_no_pass = test_client.post(Path, headers={'Authorization': f'Basic :{password}'})
    
    assert response_none.json['messages'][0]['code'] == 'AR0002'
    assert response_none.json['messages'][0]['text'] == 'Username and Password Required'
    assert response_no_user.json['messages'][0]['code'] == 'AR0002'
    assert response_no_user.json['messages'][0]['text'] == 'Username and Password Required'
    assert response_no_pass.json['messages'][0]['code'] == 'AR0002'
    assert response_no_pass.json['messages'][0]['text'] == 'Username and Password Required'

def test_a_user_can_register(test_client):
 
    credentials = b64encode(b'TEST1:barkbark').decode('utf-8')

    response = test_client.post('/auth/register',headers={'Authorization': f'Basic {credentials}'}, follow_redirects=True)
    print('test_a_user_can_register',response.json)