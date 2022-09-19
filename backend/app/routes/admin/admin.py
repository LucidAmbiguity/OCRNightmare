""" ADMIN Route Controller """

from typing import  TYPE_CHECKING
from ._my_format import _my_format


from app.routes.admin import admin  # type: ignore[no-redef] # pylint: disable=import-self

from app.constants.ADMIN import ADMIN

from .users import users

admin.register_blueprint(users, url_prefix='/users') # type: ignore[attr-defined]


if TYPE_CHECKING:
    from flask import Response
    # from app.types import


@admin.route('/', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
@admin.route('', methods=['GET', 'POST']) #type: ignore[attr-defined, misc]
def admin_root()->'Response':
    """Root route of Auth Module"""

    return _my_format(ADMIN.ROOT,code=200)
