""" Module return Format """

from typing import Optional, Union
from flask import  make_response,Response


def _format(
        result:Union[dict,bool,None],
        status:str='OK',
        code:int=200,
        messages:Optional[list[tuple[str,str]]]=None,
    )->Response:

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
    resp = make_response(
        result_,
        code,
        {'WWW.Authentication': 'Basic realm: "login required"'},
    ) # type: ignore[misc]
    # resp.set_cookie(
    #     'token', value=token, max_age=60*30,secure=False, httponly=True)
    return resp
