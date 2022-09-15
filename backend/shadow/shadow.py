"""OCRN project manager thingy. Inspired by php artisan"""

import os
import sys
from dotenv import load_dotenv
load_dotenv('.env')
backend = os.environ.get('PYTHONPATH') 


def make_route_init_file(route_name):
    result = []
    result.append(f'""" {route_name} BluePrint Module """\n')
    result.append(f'from flask import Blueprint\n')
    result.append(f'{route_name} = Blueprint("{route_name}", __name__,)\n')
    result.append(f'from .{route_name} import {route_name} # pylint: disable=wrong-import-position\n')
    return result

def make_route_file(route_name):
    result = []
    result.append(f'from app.routes.{route_name} import {route_name} # pylint: disable=import-self\n')
    result.append(f'from ._format import _format\n\n')
    result.append(f'def admin_root():\n')
    result.append(f'   """Root route of {route_name} Module"""\n')
    result.append(f'\n\n')
    result.append(f'    return _my_format({route_name.upper()}.ROOT,code=200)\n')
    
    return result


def make_route(route_name):

    print(backend)
    location = os.path.join(backend, 'app/routes/', route_name)
    os.mkdir(location)
    init_file_name = f'{location}/__init__.py'
    init_file = make_route_init_file(route_name)
    with open(init_file_name,'w') as out_file:
        for line in init_file:
            out_file.write(line)

    route_file_name = f'{location}/{route_name}.py'
    route_file = make_route_file(route_name)
    with open(route_file_name,'w') as out_file:
        for line in route_file:
            out_file.write(line)
    

def parse_args(args):
    action_1,action_2 = args[1].split(':')
    result_name = args[2]
    return action_1, action_2, result_name



def main() -> int:
    """Echo the input arguments to standard output"""
    actions = {
        'make': {
            'route': make_route
        }
    }
    action_1, action_2, result_name = parse_args(sys.argv)

    actions[action_1][action_2](result_name)

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit



# chdir





# OCR_BASE = 'instance/data'
# a = dotenv_values('.env')
# print(a)
# dircontents = os.listdir()
# print(dircontents)