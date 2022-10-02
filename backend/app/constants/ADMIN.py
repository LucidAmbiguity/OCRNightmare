""" Constants for the ADMIN Codes """
# # System Codes
# pylint: disable=invalid-name
from app.types import ApiResp

class ADMIN():
    """ Admin Responses """

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
    class Rollback:
        Error_ = ApiResp('ADMU0013', lambda x: f'Roll Back of {x} Failed: Wrong Status.')
        Delete_ = ApiResp('ADMU0014', lambda x: f'Project {x} : Has been deleted.')
        RB_1_ = ApiResp('ADMU0015', lambda x: f'Roll Back {x} from 1: Successful.')
        RB_2_ = ApiResp('ADMU0024', lambda x: f'Roll Back {x} from 2: Successful.')
        RB_3_ = ApiResp('ADMU0034', lambda x: f'Roll Back {x} from 3: Successful.')
        RB_4_ = ApiResp('ADMU0044', lambda x: f'Roll Back {x} from 4: Successful.')

