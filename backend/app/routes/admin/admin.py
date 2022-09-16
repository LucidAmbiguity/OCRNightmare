""" ADMIN Route Controller """

# import uuid
from typing import Optional, TYPE_CHECKING
from ._format import _format
# from flask import request, current_app


from app.routes.admin import admin # pylint: disable=import-self
# from app.repositories.user_repo import UserRepo
# from app.types.my_types import NewUserTup
from app.constants.AUTH import REGISTER
from app.constants.ADMIN import ADMIN
# from app.services.login_s import login_service

from .users import users

admin.register_blueprint(users, url_prefix='/users')


if TYPE_CHECKING:
    from flask import Response
    # from app.types import


def _my_format(api_code:tuple, result:Optional[dict] = None,x=None,code:int=401)->'Response':
    print('result: ',api_code,result)
    if x is None:
        return _format(
            result,
            code = code,
            messages = [
                (api_code[0], api_code[1]),
                REGISTER.Realm],
        )
    return _format(
            result,
            code = code,
            messages = [(api_code[0], api_code[1](x)),REGISTER.Realm],
        )


@admin.route('/', methods=['GET', 'POST'])
@admin.route('', methods=['GET', 'POST'])
def admin_root():
    """Root route of Auth Module"""

    return _my_format(ADMIN.ROOT,code=200)
