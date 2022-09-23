# pylint: disable=unused-argument
"""Test the default admin users uid route '/admin/users/<uid>' """

# from base64 import b64encode
from unittest.mock import patch
from app.types.my_types import MockUserAlso

from tests.helpers import (
    is_response_shape_admin,
)
# pylint: disable=invalid-name unused-import
Path = '/admin/users/'
user_mock1 = MockUserAlso(1,'pub_id1','name1',False)
@patch('app.repositories.user_repo.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_page_get_returns_200(a, test_client):
    _path = Path+'1'
    response = test_client.get(_path)
    assert response.status_code == 200


@patch('app.repositories.user_repo.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_response_shape(a, test_client):
    _path = Path+'1'
    response = test_client.get(_path)
    assert response.status_code == 200
    assert is_response_shape_admin(response.json)


@patch('app.repositories.user_repo.DBUserI.get_user_by_id', return_value = user_mock1)
def test_admin_users_uid_gets_a_user(a, test_client):
    _path = Path+'1'
    response = test_client.get(_path)
    assert response.json['result']['user'] == {
            'admin': False, 'id': 1, 'name': 'name1', 'public_id': 'pub_id1'
        }

user_mock2 = None
@patch('app.interfaces.db_user_if.DBUserI.get_user_by_id', return_value = user_mock2)
def test_admin_users_uid_returns_404_when_uid_not_found(a, test_client):
    _path = Path+'1'
    response = test_client.get(_path)
    assert response.status_code == 404

