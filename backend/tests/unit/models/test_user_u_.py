"""Model Unit TEST FILE"""
# pylint: disable=invalid-name



from unittest.mock import patch
from app.models import User, user_schema, users_schema
from app.interfaces.db_user_if import DBUserI
from app.types.my_types import NewUserTup
# from werkzeug.security import generate_password_hash, check_password_hash
from tests.helpers import attr_counter, valid_uuid


def test_user_has_expected_attributes():
    """test_user_has_expected_attributes"""
    user = User()
    assert hasattr(user,'id')
    assert hasattr(user,'public_id')
    assert hasattr(user,'name')
    assert hasattr(user,'password')
    assert hasattr(user,'admin')

    # from db.model
    assert hasattr(user,'metadata')
    assert hasattr(user,'query_class')
    assert hasattr(user,'registry')
    #count check will fail if attributes added to model.
    attr_count = attr_counter(user)
    assert attr_count == 9 # plus 'query'


@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def test_new_user_encrypts_password_generates_public_id_and_sets_admin_False(a,b,c): # pylint: disable=unused-argument
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """

    username,password = 'Rufus', '!password123'
    nut = NewUserTup(None,username,password,None)
    new_user1 = DBUserI().new_user(nut)

    assert new_user1.name == 'Rufus'
    assert new_user1.password != '!password123'
    assert valid_uuid(new_user1.public_id)
    assert new_user1.admin is False

def test_user_schema(new_user1):
    """test text line schema"""

    assert user_schema.dump(new_user1) == {'public_id': '1b6dd37d-37f1-41c0-a441-c644f2d9525c', 'name': 'Rufus', 'admin': False, 'id': 1} # pylint: disable=line-too-long

def test_users_schema(new_user1,new_user2):
    """test text lines schema"""
     # pylint: disable=line-too-long
    users = [new_user1,new_user2]
    print(users)
    assert users_schema.dump(users) == [
      {'public_id': '1b6dd37d-37f1-41c0-a441-c644f2d9525c', 'name': 'Rufus', 'admin': False, 'id': 1},
      {'public_id': '4aac1ea8-f877-473e-b38b-e7bf27747c17', 'name': 'Murphy', 'admin': False, 'id': 2},
    ]
