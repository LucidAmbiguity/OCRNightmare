""" Test Helper Functions """


import re
from typing import Any


def is_response_shape_auth_error(res_object):
    return all([
        'code'     in res_object.keys(),
        'messages' in res_object.keys(),
        'result'   in res_object.keys(),
        'status'   in res_object.keys(),

        'code'     in res_object['messages'][0].keys(),
        'text'     in res_object['messages'][0].keys(),
        'code'     in res_object['messages'][1].keys(),
        'text'     in res_object['messages'][1].keys(),

        'links'    in res_object['result'].keys(),

        'login'    in res_object['result']['links'].keys(),
        'register' in res_object['result']['links'].keys(),
    ])


def is_response_shape_auth_success(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        'register'  in res_object['result'].keys(),
        'public_id' in res_object['result'].keys(),
    ])


def is_response_shape_admin(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        isinstance(res_object['result'],dict)
    ])


def is_response_shape_ocrn(res_object):
    return all([
        'code'     in res_object.keys(),
        'messages' in res_object.keys(),
        'result'   in res_object.keys(),
        'status'   in res_object.keys(),

        'code'     in res_object['messages'][0].keys(),
        'text'     in res_object['messages'][0].keys(),
        'code'     in res_object['messages'][1].keys(),
        'text'     in res_object['messages'][1].keys(),

        isinstance(res_object['result'],dict)
    ])

def is_response_shape_ocrn_many_projects(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        'projects'  in res_object['result'].keys(),

        isinstance(res_object['result'],dict)
    ])

def is_response_shape_ocrn_one_project(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        'project'  in res_object['result'].keys(),

        isinstance(res_object['result'],dict)
    ])


def is_response_shape_ocrn_error(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        'errors'  in res_object['result'].keys(),

        isinstance(res_object['result'],dict)
    ])


def valid_uuid(uuid:str)->bool:
    """Check that uuid is a valid uuid4 value

    Args:
        uuid (string): uuid as a string

    Returns:
        boolean: True if valid uuid4
    """
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}', re.I) # pylint: disable=line-too-long
    match = regex.match(uuid)
    return bool(match)


def attr_counter(obj:Any)->int:
    obj_dir=dir(obj) # type: ignore[misc]
    count = 0
    for val in obj_dir:
        if '_' == val[0]:
            continue
        count += 1
        print('attr_counter',val)
    return count