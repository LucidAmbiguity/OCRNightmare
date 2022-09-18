""" Module return Format """

from typing import Any, Optional, Union
from flask import  make_response,Response

from app.constants.OCRN import OCRN


def _my_format(api_code:tuple, result:Optional[dict] = None,x:str=None,code:int=200)->'Response':

    if x is None:
        return _format(
            result, # type: ignore[misc]
            code = code,
            messages = [
                api_code, # type: ignore[misc]
                OCRN.Realm],
        )
    return _format(
            result, # type: ignore[misc]
            code = code,
            messages = [(api_code[0], api_code[1](x)),OCRN.Realm], # type: ignore[misc]
        )




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
        {'Lucid Ambiguity': 'Ocr Nightmare'}, # type: ignore[misc]
    ) # type: ignore[misc]
    return resp

# # If need to add cookies or some thing except response to var then
# resp.set_cookie(
#     'token', value=token, max_age=60*30,secure=False, httponly=True)
