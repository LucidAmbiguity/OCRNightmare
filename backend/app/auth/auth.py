""" Authentication Route Controller """

import uuid
from typing import Optional
from flask import request


from app.auth import auth # pylint: disable=import-self
from app.repositories.user_repo import UserRepo
from app.types.my_types import NewUserTup
from app.constants import AUTH

from ._format import _format


def _my_format(api_code:tuple, result:Optional[dict] = None,x=None,code:int=401):
    if x is None:
        return _format(
            result,
            code = code,
            messages = [
                (api_code[0], api_code[1]),
                AUTH.Realm],
        )
    return _format(
            result,
            code = code,
            messages = [(api_code[0], api_code[1](x)),AUTH.Realm],
        )


@auth.route('/', methods=['GET', 'POST'])
@auth.route('', methods=['GET', 'POST'])
def auth_root():
    """Root route of Auth Module"""

    return _my_format(AUTH.ROOT,code=200)


@auth.route('/register', methods=['POST'])
def register_user():
    """Create a User"""
    request_auth = request.authorization
    if (       not request_auth
            or not request_auth.username
            or not request_auth.password):
        return _my_format(AUTH.Missing)

    username = request_auth.username
    if len(username) < 3 :
        return _my_format(AUTH.ShortUser_,x=username)

    user = UserRepo().get_user_by_username(username)
    if user is not None:
        return _my_format(AUTH.BadName_,x=username)

    password = request_auth.password
    if len(password) < 8 :
        return _my_format(AUTH.ShortPass)

    new_user_t = NewUserTup(str(uuid.uuid4()), username, password, False)
    new_user = UserRepo().new_user(new_user_t)

    if new_user is None:
        return _my_format(AUTH.CreateError)

    result_ = {
            'register': 'success',
            'public_id': new_user['public_id'],
        }

    return _my_format(AUTH.SUCCESS,result=result_,code=200)
