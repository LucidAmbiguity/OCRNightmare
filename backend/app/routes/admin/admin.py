""" ADMIN Route Controller """

# import uuid
from typing import Optional, TYPE_CHECKING
from ._format import _format
# from flask import request, current_app


from app.routes.admin import admin  # type: ignore[no-redef] # pylint: disable=import-self
# from app.repositories.user_repo import UserRepo
# from app.types.my_types import NewUserTup
from app.constants.AUTH import REGISTER
from app.constants.ADMIN import ADMIN
# from app.services.login_s import login_service

from .users import users

admin.register_blueprint(users, url_prefix='/users') # type: ignore[attr-defined]


if TYPE_CHECKING:
    from flask import Response
    # from app.types import


def _my_format(api_code:tuple, result:Optional[dict] = None,x:str=None,code:int=401)->'Response':

    if x is None: # type: ignore[misc]
        return _format(
            result, # type: ignore[misc]
            code = code,
            messages = [
                (api_code[0], api_code[1]), # type: ignore[misc]
                REGISTER.Realm],
        )
    return _format(
            result, # type: ignore[misc]
            code = code,
            messages = [(api_code[0], api_code[1](x)),REGISTER.Realm], # type: ignore[misc]
        )


@admin.route('/', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
@admin.route('', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
def admin_root()->'Response':
    """Root route of Auth Module"""

    return _my_format(ADMIN.ROOT,code=200)
