"""Mocked Models"""

from base64 import b64encode
import pytest

from app.types.my_types import NewUserTup


@pytest.fixture(scope='module')
# @patch('uuid.uuid4', return_value = '1b6dd37d-37f1-41c0-a441-c644f2d9525c')
def new_user1():  # pylint: disable=unused-argument
    """
    Returns:
        User: User model with mock data
    """
    
    username,password,public_id = 'Rufus', '!password123','1b6dd37d-37f1-41c0-a441-c644f2d9525c'
    new_user = NewUserTup(public_id, username, password, False)

    return new_user



@pytest.fixture(scope='module')
def user1_creds():  # pylint: disable=unused-argument
    username = 'TEST1'
    password = 'barkbark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')
    return (credentials,username)

