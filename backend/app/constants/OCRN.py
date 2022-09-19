""" Constants for the AUTH Codes """
# # System Codes
# pylint: disable=invalid-name




from app.types import ApiResp



class OCRN():
    Realm = ApiResp('OCRN0001', 'OCRN by Lucid Ambiguity')
    ROOT =  ApiResp('OCRN0002', 'OCRN Main Application Root')
    UserDel_ = ApiResp('OCRN0001', lambda x: f'User {x} : Has been deleted')
    # UserDel_: tuple[str, Callable[[str],str]] = ('OCRN0001', lambda x: f'User {x} : Has been deleted')
