# pylint: disable=unused-argument
"""Test the default admin users route '/admin/users' """

# from base64 import b64encode
from unittest.mock import patch
from app.types.my_types import MockUserAlso

from tests.helpers import (
    is_response_shape_admin,
)
# pylint: disable=invalid-name unused-import
Path = '/admin/users'
user_mock1 = MockUserAlso(1,'pub_id1','name1',False)
user_mock2 = MockUserAlso(2,'pub_id2','name2',False)

@patch('app.interfaces.db_user_if.DBUserI.get_all_users', return_value = [user_mock1,user_mock2])
def test_admin_users_page_get_returns_200(a, test_client):
    response = test_client.get(Path)
    assert response.status_code == 200


@patch('app.interfaces.db_user_if.DBUserI.get_all_users', return_value = [user_mock1,user_mock2])
def test_admin_users_response_shape(a, test_client):
    response = test_client.get(Path)
    assert response.status_code == 200
    assert is_response_shape_admin(response.json)

@patch('app.interfaces.db_user_if.DBUserI.get_all_users', return_value = [user_mock1,user_mock2])
def test_admin_users_gets_list_of_users(a, test_client):
    response = test_client.get(Path)
    assert response.json['result']['users'] == [
        {'admin': False, 'id': 1, 'name': 'name1', 'public_id': 'pub_id1'},
        {'admin': False, 'id': 2, 'name': 'name2', 'public_id': 'pub_id2'}
    ]

