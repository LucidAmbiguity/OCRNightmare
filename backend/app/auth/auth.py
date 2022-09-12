"""Authentication Module"""

from flask import request
from app.auth import auth  # pylint: disable=import-self


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


@auth.route('/register', methods=['POST'])  
def register_user():
    """Create a User"""
    request_auth = request.authorization
    print('auth', request_auth)
    if (not request_auth
            or not request_auth.username
            or not request_auth.password):
        return _format(
            None,
            code=401,
            messages = [('AR0002','Username and Password Required'),
                        ('A00003',"Basic realm: 'login required'")],
            ), 401, {'WWW.Authentication': "Basic realm: 'login required'"} # type: ignore[misc]  # pylint: disable=line-too-long

    # username = request_auth.username
    # password = request_auth.password
    return {
            'code': 200,
            'messages':  [
                {
                'code': 'A00010',
                'text': 'Successful Login'
                },
               
            ],
            'result': {},
            'status': 'OK'
            }
   