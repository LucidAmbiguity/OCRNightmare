""" Data Base RAW Interface for testing"""

from app.models import User



class DBInterfaceRaw:

    def new_user_raw(self)->User:
        return  User()
