"""My custom Types"""

from typing import   NamedTuple, TypedDict
from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from app.models import ColIndex





class NewUserTup(NamedTuple):
    public_id: str
    name: str
    password: str
    admin: bool

UserT = TypedDict(
    'UserT', {
        'id': int,
        'public_id': int,
        'name': str,
        'admin': bool,
    })