"""OCRN project manager thingy. Inspired by php artisan"""

import os
import sys
from dotenv import load_dotenv
load_dotenv('.env')
backend = os.environ.get('PYTHONPATH')

# pylint: disable=f-string-without-interpolation
def make_route_init_file(path,route_name):
    result = []
    if path == '':
        result.append(f'""" {route_name} BluePrint Module """\n')
        result.append(f'from flask import Blueprint\n')
        result.append(f'{route_name} = Blueprint("{route_name}", __name__,)\n')
        result.append(f'from .{route_name} import {route_name} # pylint: disable=wrong-import-position\n')
    else:
        result.append(f'""" {path} {route_name} BluePrint Module """\n')
        result.append(f'from flask import Blueprint\n')
        result.append(f'{route_name} = Blueprint("{route_name}", __name__,)\n')
        result.append(f'from .{route_name} import {route_name} # pylint: disable=wrong-import-position\n')
    return result

def make_route_file(path,route_name):
    result = []
    if path == '':

        result.append(f'""" {route_name} route Controller """')
        result.append(f'')
        result.append(f'')
        result.append(f'from app.routes.{route_name} import {route_name} # pylint: disable=import-self\n')
        result.append(f'from ._format import _my_format\n\n')
        result.append(f"@{route_name}.route('/', methods=['GET', 'POST'])\n")
        result.append(f"@{route_name}.route('', methods=['GET', 'POST'])\n")
        result.append(f'def {route_name}_root():\n')
        result.append(f'    """Root route of {route_name} Module"""\n')
        result.append(f'\n\n')
        result.append(f'    return _my_format({route_name.upper()}.ROOT,code=200)\n')
    else:
        result.append(f'""" {path} {route_name} route Controller """')
        result.append(f'')
        result.append(f'')
        result.append(f'from app.routes.{path}.{route_name} import {route_name} # pylint: disable=import-self\n')
        result.append(f'from .._format import _format\n\n')
        result.append(f"@{route_name}.route('/', methods=['GET', 'POST'])\n")
        result.append(f"@{route_name}.route('', methods=['GET', 'POST'])\n")
        result.append(f'def {route_name}_root():\n')
        result.append(f'    """Root route of {path} {route_name} Module"""\n')
        result.append(f'\n\n')
        result.append(f'    return _my_format({route_name.upper()}.ROOT,code=200)\n')

    return result
# pylint: enable=f-string-without-interpolation

def make_route(path,route_name):

    print(backend)
    if path == '':
        location = os.path.join(backend, 'app/routes/', route_name)
    else:
        location = os.path.join(backend, f'app/routes/{path}/', route_name)
    os.mkdir(location)
    init_file_name = f'{location}/__init__.py'
    init_file = make_route_init_file(path,route_name)
    with open(init_file_name,'w',encoding='utf-8') as out_file:
        for line in init_file:
            out_file.write(line)

    route_file_name = f'{location}/{route_name}.py'
    route_file = make_route_file(path,route_name)
    with open(route_file_name,'w',encoding='utf-8') as out_file:
        for line in route_file:
            out_file.write(line)


def parse_args(args):
    action_1,action_2 = args[1].split(':')
    if '.' in args[2]:
        path,result_name = args[2].split('.')
    else:
        path = ''
        result_name = args[2]
    return action_1, action_2, path ,result_name



def main() -> int:
    """Echo the input arguments to standard output"""
    actions = {
        'make': {
            'route': make_route
        }
    }
    action_1, action_2, path ,result_name = parse_args(sys.argv)
    print(action_1, action_2, path ,result_name)
    actions[action_1][action_2](path,result_name)

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit



# chdir





# OCR_BASE = 'instance/data'
# a = dotenv_values('.env')
# print(a)
# dircontents = os.listdir()
# print(dircontents)
