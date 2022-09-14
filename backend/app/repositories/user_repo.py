"""A User Repository"""
# Possibly unneeded be this small repo
# However its good practice for untangling the rest of the app

from app.models import (
    user_schema,
    # users_schema,
)
# from app.ocrnightmare.helpers.my_types import UserT
from app.interfaces.db_user_if import DBUserI

from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from app.models import User
    from app.types import UserT,NewUserTup


class UserRepo:
    """A User Repository"""

    def _return_logic(self,user_db:Optional['User'])->Optional['UserT']:
        if user_db is None:
            return None
        user_: 'UserT' = user_schema.dump(user_db)
        return user_

    def __init__(self, db_u_i=DBUserI) ->None:
        self._db_u_i = db_u_i()

    def get_user_by_username(self, username: str)->Optional['UserT']:
        user_db = self._db_u_i.get_user_by_username(username)
        return self._return_logic(user_db)

    def new_user(self,new_user_t:'NewUserTup')->Optional['UserT']:
        user_db = self._db_u_i.new_user(new_user_t)
        return self._return_logic(user_db)
