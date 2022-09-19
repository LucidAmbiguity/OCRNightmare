""" Module return Format """

from typing import Optional
from flask import  Response

from app.constants.AUTH import REGISTER
from app.types.my_types import ApiResp
from app._format import _format

def _my_format(api_code:ApiResp, result:Optional[dict] = None,x:str=None,code:int=401)->'Response':

    if result is None:
        result = {'links': { # type: ignore[misc]
            'login': 'login',
            'register': 'register'
        }}

    if x is None:
        return _format(
            result = result, # type: ignore[misc]
            code = code,
            messages = [
                api_code, # type: ignore[misc]
                REGISTER.Realm
            ],
            headers = {'WWW.Authentication': 'Basic realm: "login required"'},
        )
    print('admin/_my_format')
    print(not isinstance(api_code.text,str))
    print(isinstance(api_code.text,str))
    print(api_code.text)
    if not isinstance(api_code.text,str):
        return _format(
                result = result, # type: ignore[misc]
                code = code,
                messages = [
                    ApiResp(api_code[0],
                    api_code.text(x)),REGISTER.Realm # type: ignore[misc]
                ],
                headers = {'WWW.Authentication': 'Basic realm: "login required"'},
        )
    raise ValueError('api_code.text should be str or Callable[[str],str]')

