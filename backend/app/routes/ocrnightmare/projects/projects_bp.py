""" ocrnightmare projects route Controller """


from typing import TYPE_CHECKING
from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.projects import projects_bp # type: ignore[no-redef] # pylint: disable=import-self
from .._my_format import _my_format

if TYPE_CHECKING:
    from flask import Response

@projects_bp.route('/', methods=['GET', 'POST']) # type: ignore[misc, attr-defined]
@projects_bp.route('', methods=['GET', 'POST']) # type: ignore[misc, attr-defined]
def projects_root()->'Response':
    """Root route of ocrnightmare projects Module"""


    return _my_format(OCRN.Projects,code=200)
