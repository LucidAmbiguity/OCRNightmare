""" Module return Format """

from typing import Any, Optional, Union
from flask import  make_response,Response


def _format(
        result:Union[dict[Any,Any],bool,None],
        status:str='OK',
        code:int=200,
        messages:Optional[list[tuple[str,str]]]=None,
    )->Response:

    if result is None: # type: ignore[misc]
        result = {'links': { # type: ignore[misc]
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
        'result': result, # type: ignore[misc]
    }
    resp = make_response(
        result_,
        code,
        {'WWW.Authentication': 'Basic realm: "login required"'}, # type: ignore[misc]
    ) # type: ignore[misc]
    # resp.set_cookie(
    #     'token', value=token, max_age=60*30,secure=False, httponly=True)
    return resp
