"""My custom Types"""

from dataclasses import dataclass
from typing import   Callable, NamedTuple, Optional, TypedDict, Union
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from app.models import ColIndex


AToken = str





class PassId(NamedTuple):
    password: str
    public_id: str

class PassIdNone(NamedTuple):
    password: Optional[str] = None
    public_id: Optional[str] = None


class ApiResp(NamedTuple):
    code: str
    text: Union[str,Callable[[str],str]]

class MockCount:
    _count:int
    def __init__(self,val:int)->None:
        self._count = val
    def count(self)->int:
        return self._count


class NewUserTup(NamedTuple):
    public_id: str
    name: str
    password: str
    admin: bool


# ! Why did I do this with 2 dif models.
# # one might be for admin views.
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


UserT = TypedDict(
    'UserT', {
        'id': int,
        'public_id': int,
        'name': str,
        'admin': bool,
    })


class NewProjTup(NamedTuple):
    name: str
    filename: str
    status: int

@dataclass()
class MockProject:
    id:int # pylint: disable=invalid-name
    name: str
    status: int
    filename:str
    pages: MockCount
    customers: MockCount

ProjDataT = TypedDict(
    'ProjDataT', {
        'id':int,
        'name': str,
        'status': int,
        'filename':str,
        'pages': int,
        'customers': int,
    })

ProjectT = TypedDict(
    'ProjDataT', {
        'id':int,
        'name': str,
        'status': int,
        'filename':str,
    })

class NewPageTup(NamedTuple):
    project_id: int

@dataclass()
class MockPage:
    id:int # pylint: disable=invalid-name
    project_id: int

PageT = TypedDict(
    'PageT', {
        'id':int,
        'project_id': int
    })

class NewCustomerTup(NamedTuple):
    project_id: int

@dataclass()
class MockCustomer:
    id:int # pylint: disable=invalid-name
    project_id: int

CustomerT = TypedDict(
    'CustomerT', {
        'id':int,
        'project_id': int
    })


