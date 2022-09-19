""" Constants for the ADMIN Codes """
# # System Codes
# pylint: disable=invalid-name
from app.types import ApiResp

class ADMIN():
    ROOT = ApiResp('ADM0001', 'Admin root')
    Realm = ApiResp('ADM0002', 'Admin Realm')
    Users = ApiResp('ADMU0010','List of Users retrieved.')
    User = ApiResp('ADMU0011','A user record.')
    UserDel_= ApiResp('ADMU0012', lambda x: f'User {x} : Has been deleted')

    # Missing = ('AL0012', 'Username and Password Required')
    # Failed_ = ('AL0015', lambda x: f'Login Failed for {x} : Bad username or password')
    # BadPass = ('AL0016','Bad Password')
    # CreateError = ('AL0017','creation error')
    # SUCCESS = ('AL0020','Login Successful')
