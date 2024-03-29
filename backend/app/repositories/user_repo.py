"""A User Repository"""
# Possibly unneeded be this small repo
# However its good practice for untangling the rest of the app

from app.models import (
    user_schema,
    # users_schema,
)
# from app.ocrnightmare.helpers.my_types import UserT
from app.interfaces.db_user_if import DBUserI

from typing import TYPE_CHECKING, Optional, Type, Union

from app.types.my_types import PassId, PassIdNone


if TYPE_CHECKING:
    from app.models import User
    from app.types import UserT


class UserRepo:
    """A User Repository"""
    has_user = False

    def __init__(
            self,
            username:str=None,
            uid:int=None,
            public_id:str=None,
            db_u_i:Type[DBUserI]=DBUserI,
            ) ->None:

        self._db_u_i = db_u_i()
        self._username = username
        self._id = uid
        self._public_id = public_id
        self._user_db = None

        if username:
            self._user_db = self._db_u_i.get_user_by_username(self._username)
            self._has_user()
        if uid:
            self._user_db = self._db_u_i.get_user_by_id(self._id)
            self._has_user()
        if public_id:
            self._user_db = self._db_u_i.get_user_by_public_id(self._public_id)
            self._has_user()

    def _return_logic(self,user_db:Optional['User'])->Optional['UserT']:
        if user_db is None:
            return None
        user_: 'UserT' = user_schema.dump(user_db)
        return user_

    def _has_user(self)->None:
        if self._user_db is not None:
            self.has_user = True


    def get_user(self)->Optional['UserT']:
        return self._return_logic(self._user_db)

    def get_user_password(self)->Optional[str]:
        user_db = self._db_u_i.get_user_by_username(self._username)
        if user_db is None:
            return None
        return user_db.password

    def get_user_password_and_pubid(self)->Union[PassId,PassIdNone]:
        if self._user_db is not None:
            return PassId(self._user_db.password,self._user_db.public_id)
        return PassIdNone()

    def del_user(self)->bool:
        return self._db_u_i.del_user(self._user_db)


