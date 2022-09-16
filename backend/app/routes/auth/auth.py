""" Authentication Route Controller """

import uuid
from typing import Optional, TYPE_CHECKING
from flask import request, current_app


from app.routes.auth import auth # pylint: disable=import-self
from app.repositories.user_repo import UserRepo
from app.repositories.users_repo import UsersRepo
from app.types.my_types import NewUserTup
from app.constants.AUTH import REGISTER,LOGIN
from app.services.login_s import login_service

from ._format import _format

if TYPE_CHECKING:
    from flask import Response
    # from app.types import


def _my_format(api_code:tuple, result:Optional[dict] = None,x=None,code:int=401)->'Response':
    print('result: ',api_code,result)
    if x is None:
        return _format(
            result,
            code = code,
            messages = [
                (api_code[0], api_code[1]),
                REGISTER.Realm],
        )
    return _format(
            result,
            code = code,
            messages = [(api_code[0], api_code[1](x)),REGISTER.Realm],
        )


@auth.route('/', methods=['GET', 'POST'])
@auth.route('', methods=['GET', 'POST'])
def auth_root():
    """Root route of Auth Module"""

    return _my_format(REGISTER.ROOT,code=200)


@auth.route('/register', methods=['POST'])
def register_user():
    """Create a User"""
    request_auth = request.authorization
    if (       not request_auth
            or not request_auth.username
            or not request_auth.password):
        return _my_format(REGISTER.Missing)

    username = request_auth.username
    if len(username) < 3 :
        return _my_format(REGISTER.ShortUser_,x=username)

    user = UserRepo(username=username).get_user()
    if user is not None:
        return _my_format(REGISTER.BadName_,x=username)

    password = request_auth.password
    if len(password) < 8 :
        return _my_format(REGISTER.ShortPass)

    new_user_t = NewUserTup(str(uuid.uuid4()), username, password, False)
    new_user = UsersRepo().new_user(new_user_t)

    if new_user is None:
        return _my_format(REGISTER.CreateError)

    result_ = {
            'register': 'success',
            'public_id': new_user['public_id'],
        }

    return _my_format(REGISTER.SUCCESS,result=result_,code=200)

@auth.route('/login', methods=['POST']) # type: ignore[attr-defined,misc]
def login_user()->'Response':
    """LOGIN route"""

    request_auth = request.authorization
    if (       not request_auth
            or not request_auth.username
            or not request_auth.password):
        return _my_format(LOGIN.Missing)

    access_token,pub_id = login_service(
        (
            request_auth.username,
            request_auth.password
        ),
        current_app,
    )
    print('login_user: ',access_token,pub_id)
    if access_token is None:
        return _my_format(LOGIN.Failed_,x=request_auth.username)

    result_ = {
            'login': 'Success',
            'public_id': pub_id
        }
    response = _my_format(LOGIN.SUCCESS,result=result_)
    response.set_cookie(
        'token', value=access_token, max_age=60*30,secure=False, httponly=True)
    return response

