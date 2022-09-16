""" ADMIN User Route Controller """

from typing import Optional, TYPE_CHECKING
from .._format import _format

from app.routes.admin.users import users # pylint: disable=import-self unused-import
from app.repositories.users_repo import UsersRepo
from app.constants.AUTH import REGISTER
from app.constants.ADMIN import ADMIN


if TYPE_CHECKING:
    from flask import Response

def _my_format(api_code:tuple, result:Optional[dict] = None,x=None,code:int=401)->'Response':
    print('result: ',api_code,result)
    if x is None:
        return _format(
            result,
            code = code,
            messages = [
                (api_code[0], api_code[1]),
                REGISTER.Missing],
        )
    return _format(
            result,
            code = code,
            messages = [(api_code[0], api_code[1](x)),REGISTER.Realm],
        )

@users.route('', methods=['GET', 'POST'])
def users_root():
    """Root route of admin users Module"""

    _users_ = UsersRepo().get_all_users()

    result = { 'users': _users_ }

    return _my_format(ADMIN.Users,code=200,result=result)

@users.route('/<id>', methods=['GET', 'POST'])
def users_test(id):
    pass