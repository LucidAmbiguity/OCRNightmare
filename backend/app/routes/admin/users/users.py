""" ADMIN User Route Controller """

from typing import Any, Optional, TYPE_CHECKING
from flask import abort
from .._format import _format

from app.routes.admin.users import users # type: ignore[no-redef] # pylint: disable=import-self unused-import
from app.repositories.users_repo import UsersRepo
from app.repositories.user_repo import UserRepo
from app.constants.AUTH import REGISTER
from app.constants.ADMIN import ADMIN


if TYPE_CHECKING:
    from flask import Response

def _my_format(api_code:tuple[str,str], result:Optional[dict[Any,Any]] = None,x:str=None,code:int=401)->'Response':

    if x is None:
        return _format(
            result, #type: ignore[misc]
            code = code,
            messages = [
                (api_code[0], api_code[1]),
                REGISTER.Missing],
        )
    return _format(
            result, #type: ignore[misc]
            code = code,
            messages = [(api_code[0], api_code[1](x)),REGISTER.Realm],  #type: ignore[misc,operator]
        )

@users.route('', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
def users_root()->'Response':
    """Root route of admin users Module"""

    _users_ = UsersRepo().get_all_users()

    result = { 'users': _users_ }

    return _my_format(ADMIN.Users,code=200,result=result)

@users.route('/<int:uid>', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
def users_test(uid:int)->'Response':
    _user_ = UserRepo(uid=uid).get_user()

    if _user_ is None:
        abort(404)
    result = { 'user': _user_ }

    return _my_format(ADMIN.User,code=200,result=result)



