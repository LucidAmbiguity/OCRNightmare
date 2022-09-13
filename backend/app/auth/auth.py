"""Authentication Module"""

import uuid
from flask import request
from app.auth import auth
from app.repositories.user_repo import UserRepo
from app.types.my_types import NewUserTup  # pylint: disable=import-self


@auth.route('/', methods=['GET', 'POST'])
@auth.route('', methods=['GET', 'POST'])
def auth_root():
    """Root route of App Module"""
    return {
            'code': 200,
            'messages': [
                {
                'code': 'A00001', 
                'text': 'Success.'
                }
            ],
            'result': {
                'links': {
                'login': 'login', 
                'register': 'register'
                }
            },
            'status': 'OK'
            }, 200, {'WWW.Authentication': 'Basic realm: "login required"'}


from typing import Optional, Union


def _format(
        result:Union[dict,bool,None],
        status:str='ok',
        code:int=200,
        messages:Optional[list[tuple[str,str]]]=None,
    )->dict:

    if result is None:
        result = {'links': {
        'login': 'login',
        'register': 'register'
    }}
    if messages is None:
        messages = [('','')]

    messages_ = []
    for message in messages:
        messages_.append({
            'code': message[0],
            'text': message[1],
        })

    result_ = {
        'status': status,
        'code': code,
        'messages':messages_,
        'result': result,
    }
    return result_


def _my_format(api_code:tuple, result:Optional[dict] = None,x=None):
    if x is not None:
        return _format(
            result,
            code = 401,
            messages = [(api_code[0], api_code[1])],
        )
    return _format(
            result,
            code = 401,
            messages = [(api_code[0], api_code[1](x))],
        )


@auth.route('/register', methods=['POST'])  
def register_user():
    """Create a User"""
    request_auth = request.authorization
    if (not request_auth
            or not request_auth.username
            or not request_auth.password):
        return _format(
            None,
            code=401,
            messages = [('AR0002','Username and Password Required'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    username = request_auth.username
    if len(username) < 3 :
        return _format(
            None,
            code=401,
            messages = [('AR0004',f'{username} is to short. At Least 3 characters please'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    user = UserRepo().get_user_by_username(username)
    if user is not None:
        return _format(
            None,
            code=401,
            messages = [('AR0005',f'{username} Is in use'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    password = request_auth.password
    if len(password) < 8 :

        return _format(
            None,
            code=401,
            messages = [('AR0006','Password  is to short. At Least 8 characters please'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    new_user_t = NewUserTup(str(uuid.uuid4()), username, password, False)
    new_user = UserRepo().new_user(new_user_t)

    if new_user is None:
        return _format(
            None,
            code=401,
            messages = [('AR0007','creation error'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    result_ = {
            'register': 'success',
            'public_id': new_user['public_id'],
        }
    return _format(
            result_,
            code=200,
            messages = [('AR0010','Register Successful'),
                        ('AR0003',"Basic realm: 'login required'")],
            ), 200, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

