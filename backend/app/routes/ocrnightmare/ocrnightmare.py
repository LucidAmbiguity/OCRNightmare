""" ocrnightmare route Controller """


from typing import TYPE_CHECKING
from app.routes.ocrnightmare import ocrnightmare # type: ignore[no-redef] # pylint: disable=import-self
from ._my_format import _my_format

from .projects import projects_bp

from app.constants.OCRN import OCRN

if TYPE_CHECKING:
    from flask import Response


ocrnightmare.register_blueprint(projects_bp,        url_prefix='/projects')  # type: ignore[ attr-defined]

@ocrnightmare.route('/', methods=['GET', 'POST']) # type: ignore[misc, attr-defined]
@ocrnightmare.route('', methods=['GET', 'POST']) # type: ignore[misc, attr-defined]
def ocrnightmare_root()->'Response':
    """Root route of  ocrnightmare Module"""

    result = {'data': {
                    'ocrnightmare': 'ocrnightmare root',
        }
    }
    return _my_format(OCRN.ROOT, code=200,result=result)
