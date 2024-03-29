""" ocrnightmare route Controller """


from typing import TYPE_CHECKING

from app.routes.ocrnightmare import ocrnightmare

from app.constants.OCRN import OCRN

from ._my_format import _my_format

from .bp.projects import projects_bp
from .bp.extract import extract_bp # type: ignore[no-redef] # pylint: disable=import-self
from .bp.text_lines import text_lines_bp # type: ignore[no-redef] # pylint: disable=import-self
from .bp.pages import pages_bp # type: ignore[no-redef] # pylint: disable=import-self


if TYPE_CHECKING:
    from flask import Response


ocrnightmare.register_blueprint(text_lines_bp,         url_prefix='/projects/<project_name>/text_lines')
ocrnightmare.register_blueprint(pages_bp,         url_prefix='/projects/<project_name>/pages')
ocrnightmare.register_blueprint(extract_bp,         url_prefix='/projects/<project_name>/extract')
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
