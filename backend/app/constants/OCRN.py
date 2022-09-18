""" Constants for the AUTH Codes """
# # System Codes
# pylint: disable=invalid-name




from typing import Callable


class OCRN():
    Realm = ('OCRN0001', 'OCRN by Lucid Ambiguity')
    ROOT =  ('OCRN0002', 'OCRN Main Application Root')
    # UserDel_: tuple[str, Callable[[str],str]] = ('OCRN0001', lambda x: f'User {x} : Has been deleted')
