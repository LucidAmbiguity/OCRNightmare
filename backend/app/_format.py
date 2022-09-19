""" Module return Format """

from typing import Any, Callable, Optional, Union
from flask import  make_response,Response

from app.constants.OCRN import OCRN
from app.types.my_types import ApiResp







def _format(
        result:Union[dict[Any,Any],bool,None]=None,
        status:str='OK',
        code:int=200,
        messages:Optional[list[ApiResp]]=None,
        headers:Optional[dict[str,str]]=None,
    )->Response:

    if result is None: # type: ignore[misc]
        result = {}
    if messages is None:
        messages = [ApiResp('','')]

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
        headers, # type: ignore[misc]
    ) # type: ignore[misc]
    return resp

# # If need to add cookies or some thing except response to var then
# resp.set_cookie(
#     'token', value=token, max_age=60*30,secure=False, httponly=True)
