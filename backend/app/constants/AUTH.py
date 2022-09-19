""" Constants for the AUTH Codes """
# pylint: disable=invalid-name


from app.types import ApiResp




class REGISTER():
    ROOT = ApiResp('A00001', 'authentication root')
    Missing = ApiResp('AR0002', 'Username and Password Required')
    Realm = ApiResp('AR0003', "Basic realm: 'login required'")
    ShortUser_ = ApiResp('AR0004', lambda x: f'{x} is to short. At Least 3 characters please')
    BadName_ = ApiResp('AR0005', lambda x: f'{x} Is in use')
    ShortPass = ApiResp('AR0006','Password  is to short. At Least 8 characters please')
    CreateError = ApiResp('AR0007','creation error')
    SUCCESS = ApiResp('AR0010','Register Successful')

class LOGIN():
    Missing = ApiResp('AL0012', 'Username and Password Required')
    Failed_ = ApiResp('AL0015', lambda x: f'Login Failed for {x} : Bad username or password')
    BadPass = ApiResp('AL0016','Bad Password')
    CreateError = ApiResp('AL0017','creation error')
    SUCCESS = ApiResp('AL0020','Login Successful')


