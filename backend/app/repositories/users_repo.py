"""A User Repository"""
# Possibly unneeded be this small repo
# However its good practice for untangling the rest of the app

from app.models import (
    user_schema,
    users_schema,
)
# from app.ocrnightmare.helpers.my_types import UserT
from app.interfaces.db_user_if import DBUserI

from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from app.models import User
    from app.types import UserT,NewUserTup


class UsersRepo:
    """A User Repository"""

    def _return_logic(self,user_db:Optional['User'])->Optional['UserT']:
        if user_db is None:
            return None
        user_: 'UserT' = user_schema.dump(user_db)
        return user_

    def _has_user(self)->None:
        if self._user_db is not None:
            self.has_user = True

    def __init__(
            self,
            username:str=None,
            uid:int=None,
            public_id:str=None,
            db_u_i=DBUserI,
            ) ->None:

        self._db_u_i = db_u_i()
        self._username = username
        self._id = uid
        self._public_id = public_id
        self._user_db = None
        self.has_user = False
        if username:
            self._user_db = self._db_u_i.get_user_by_username(self._username)
            self._has_user()
        if uid:
            self._user_db = self._db_u_i.get_user_by_id(self._id)
            self._has_user()
        if public_id:
            self._user_db = self._db_u_i.get_user_by_public_id(self._public_id)
            self._has_user()

    def get_user_by_username(self)->Optional['UserT']:
        user_db = self._db_u_i.get_user_by_username(self._username)
        return self._return_logic(user_db)

    def new_user(self,new_user_t:'NewUserTup')->Optional['UserT']:
        user_db = self._db_u_i.new_user(new_user_t)
        return self._return_logic(user_db)

    def get_all_users(self)->list[Optional['UserT']]:
        users_db: list['User'] = self._db_u_i.get_all_users()
        users_: list[Optional['UserT']] = users_schema.dump(users_db)
        return users_ # type: ignore[misc]
        