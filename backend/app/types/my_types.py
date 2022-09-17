"""My custom Types"""

from dataclasses import dataclass
from typing import   NamedTuple, Optional, TypedDict
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from app.models import ColIndex
AToken = str


class MockUser(NamedTuple):
    public_id: str
    name: str
    password: str
    admin: bool




@dataclass()
class MockUserAlso:
    id: int # pylint: disable=invalid-name
    public_id: str
    name: str
    admin: bool





class PassId(NamedTuple):
    password: str
    public_id: str

class PassIdNone(NamedTuple):
    password: Optional[str] = None
    public_id: Optional[str] = None

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
