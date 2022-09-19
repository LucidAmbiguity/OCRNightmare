""" Test Helper Functions """


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

def is_response_shape_ocrn_projects(res_object):
    return all([
        'code'      in res_object.keys(),
        'messages'  in res_object.keys(),
        'result'    in res_object.keys(),
        'status'    in res_object.keys(),

        'code'      in res_object['messages'][0].keys(),
        'text'      in res_object['messages'][0].keys(),
        'code'      in res_object['messages'][1].keys(),
        'text'      in res_object['messages'][1].keys(),

        'data'      in res_object['result'].keys(),

        isinstance(res_object['result'],dict)
    ])
