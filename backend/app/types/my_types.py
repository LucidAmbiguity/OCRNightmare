"""My custom Types"""

from dataclasses import asdict, astuple, dataclass, asdict
from typing import   NamedTuple, TypedDict
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
    id:int
    public_id: str
    name: str
    admin: bool





class PassId(NamedTuple):
    password: str
    public_id: str

class PassIdNone(NamedTuple):
    password: str=None
    public_id: str=None

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
