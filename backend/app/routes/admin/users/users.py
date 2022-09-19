""" ADMIN User Route Controller """

from typing import  TYPE_CHECKING
from flask import abort
from .._my_format import _my_format
from app.routes.admin.users import users # type: ignore[no-redef] # pylint: disable=import-self unused-import
from app.repositories.users_repo import UsersRepo
from app.repositories.user_repo import UserRepo
from app.constants.ADMIN import ADMIN


if TYPE_CHECKING:
    from flask import Response


@users.route('', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
def users_root()->'Response':
    """Root route of admin users Module"""

    _users_ = UsersRepo().get_all_users()

    result = { 'users': _users_ }

    return _my_format(ADMIN.Users,code=200,result=result)

@users.route('/<int:uid>', methods=['GET']) #type: ignore[attr-defined, misc]
def users_test(uid:int)->'Response':
    _user_ = UserRepo(uid=uid).get_user()

    if _user_ is None:
        abort(404)
    result = { 'user': _user_ }

    return _my_format(ADMIN.User,code=200,result=result)

@users.route('/<int:uid>', methods=['DELETE']) # type: ignore[attr-defined,misc]
def delete_user(uid:int)->'Response':

    success =  UserRepo(uid=uid).del_user()

    if not success:
        abort(404)
    return _my_format(ADMIN.UserDel_,code=200,x=str(uid))


@users.route('/<pub_id>', methods=['DELETE']) # type: ignore[attr-defined,misc]
def delete_user_by_pub_id(pub_id:str)->'Response':

    success =  UserRepo(public_id=pub_id).del_user()
    if not success:
        abort(404)

    return _my_format(ADMIN.UserDel_,code=200,x=pub_id)

