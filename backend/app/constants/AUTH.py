""" Constants for the AUTH Codes """
# # System Codes
# pylint: disable=invalid-name




from typing import Callable


class REGISTER():
    ROOT = ('A00001', 'authentication root')
    Missing = ('AR0002', 'Username and Password Required')
    Realm = ('AR0003', "Basic realm: 'login required'")
    ShortUser_: tuple[str, Callable[[str],str]] = ('AR0004', lambda x: f'{x} is to short. At Least 3 characters please')
    BadName_: tuple[str, Callable[[str],str]] = ('AR0005', lambda x: f'{x} Is in use')
    ShortPass = ('AR0006','Password  is to short. At Least 8 characters please')
    CreateError = ('AR0007','creation error')
    SUCCESS = ('AR0010','Register Successful')

class LOGIN():
    Missing = ('AL0012', 'Username and Password Required')
    Failed_: tuple[str, Callable[[str],str]] = ('AL0015', lambda x: f'Login Failed for {x} : Bad username or password')
    BadPass = ('AL0016','Bad Password')
    CreateError = ('AL0017','creation error')
    SUCCESS = ('AL0020','Login Successful')


