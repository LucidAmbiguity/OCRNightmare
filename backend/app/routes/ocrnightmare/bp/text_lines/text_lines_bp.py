""" ocrnightmare text_lines route Controller """


# from flask import request,current_app,abort



from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.bp.text_lines import text_lines_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.repositories.project_repo import ProjectRepo

from typing import TYPE_CHECKING

from ..._my_format import _my_format


if TYPE_CHECKING:
    from flask import Response

@text_lines_bp.route('', methods=['GET']) # type: ignore[misc, attr-defined]
def index(project_name:str)->'Response':
    """Root route of ocrnightmare text_lines Module"""
    text_line_list = ProjectRepo(project_name).get_all_text_lines()

    result = {'text_lines': text_line_list}
    return _my_format(OCRN.Projects, result=result ,code=200  )
