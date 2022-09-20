"""Mocked Models"""

from base64 import b64encode

import pytest


@pytest.fixture(scope='module')
def user1_creds():  # pylint: disable=unused-argument
    username = 'TEST1'
    password = 'barkbark'
    my_creds = f'{username}:{password}'
    my_creds_ = bytes(my_creds, 'utf-8')
    credentials = b64encode(my_creds_).decode('utf-8')
    return (credentials,username)

