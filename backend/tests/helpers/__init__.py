""" Test Helper Functions """


def is_response_shape_error(res_object):
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


def is_response_shape_success(res_object):
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
