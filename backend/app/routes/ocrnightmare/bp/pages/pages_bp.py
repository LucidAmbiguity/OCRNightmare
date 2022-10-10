""" ocrnightmare pages route Controller """


# from flask import request,current_app,abort



from flask import abort
from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.bp.pages import pages_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.repositories import ProjectRepo

from typing import TYPE_CHECKING

from ..._my_format import _my_format


if TYPE_CHECKING:
    from flask import Response

@pages_bp.route('', methods=['GET']) # type: ignore[misc, attr-defined]
def index(project_name)->'Response':

    page_list = ProjectRepo(project_name).get_all_pages()

    result = {'pages': page_list}
    return _my_format(OCRN.Pages, result=result ,code=200  )

@pages_bp.route('/<int:page_id>', methods=['GET']) # type: ignore[misc, attr-defined]
def a_page(project_name,page_id)->'Response':

    page = ProjectRepo(project_name).get_page(page_id)
    if page is None:
        abort(404)

    result = {'page': page}
    return _my_format(OCRN.Page, result=result ,code=200  )

@pages_bp.route('/<int:page_id>/w_tl', methods=['GET']) # type: ignore[misc, attr-defined]
def a_page_w_text_lines(project_name,page_id)->'Response':

    page = ProjectRepo(project_name).get_page_w_text(page_id)
    if page is None:
        abort(404)

    result = {'page': page}
    return _my_format(OCRN.Page, result=result ,code=200  )