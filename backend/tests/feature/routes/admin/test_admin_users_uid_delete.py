# pylint: disable=unused-argument
"""
    Test the admin users uid delete route
        '/admin/users/<uid>/delete'
"""

from unittest.mock import patch
from app.types.my_types import MockUserAlso

from tests.helpers import (
    is_response_shape_admin,
)

# pylint: disable=invalid-name unused-import

Path = '/admin/users/1'


user_mock1 = MockUserAlso(1,'pub_id1','name1',False)
@patch('app.interfaces.db_user_if.DBUserI.del_user', return_value = True)
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_delete_page_get_returns_200(a,b, test_client):
    response = test_client.delete(Path)
    assert response.status_code == 200


@patch('app.interfaces.db_user_if.DBUserI.del_user', return_value = True)
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_delete_response_shape(a,b, test_client):
    response = test_client.delete(Path)
    assert response.status_code == 200
    assert is_response_shape_admin(response.json)

@patch('app.interfaces.db_user_if.DBUserI.del_user', return_value = True)
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_delete_deletes_a_user(a,b, test_client):
    response = test_client.delete(Path)
    assert response.json['messages'][0]['text'] == 'User 1 : Has been deleted'

user_mock2 = None
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_id', return_value = user_mock2)
def test_admin_users_uid_delete_returns_404_when_uid_not_found(a, test_client):
    response = test_client.get(Path)
    assert response.status_code == 404

