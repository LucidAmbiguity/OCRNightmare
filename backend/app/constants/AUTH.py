""" Constants for the AUTH Codes """
# # System Codes
# pylint: disable=invalid-name

ROOT = ('A00001', 'authentication root')
Missing = ('AR0002', 'Username and Password Required')
Realm = ('AR0003', "Basic realm: 'login required'")
ShortUser_ = ('AR0004', lambda x: f'{x} is to short. At Least 3 characters please')
BadName_ = ('AR0005', lambda x: f'{x} Is in use')
ShortPass = ('AR0006','Password  is to short. At Least 8 characters please')
CreateError = ('AR0007','creation error')
SUCCESS = ('AR0010','Register Successful')



