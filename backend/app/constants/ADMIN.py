""" Constants for the ADMIN Codes """
# # System Codes
# pylint: disable=invalid-name

class ADMIN():
    ROOT = ('ADM0001', 'Admin root')
    Users = ('ADMU0010','List of Users retrieved.')
    User = ('ADMU0011','A user record.')
    UserDel_= ('ADMU0012', lambda x: f'User {x} : Has been deleted')

    # Missing = ('AL0012', 'Username and Password Required')
    # Failed_ = ('AL0015', lambda x: f'Login Failed for {x} : Bad username or password')
    # BadPass = ('AL0016','Bad Password')
    # CreateError = ('AL0017','creation error')
    # SUCCESS = ('AL0020','Login Successful')
