""" ocrnightmare extract route Controller """

from flask import abort
from typing import TYPE_CHECKING

from app.routes.ocrnightmare.bp.extract import extract_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.constants.OCRN import OCRN

# import app.services.extraction_s as xtract_s
from app.services.extraction_s import extraction_s
from ..._my_format import _my_format


if TYPE_CHECKING:
    from flask import Response


EXTRACT = OCRN.Extract


@extract_bp.route('', methods=['POST'])
def extract_root(project_name:str)->'Response':
    """Extract raw data from supplied PDF"""

    proj_data = extraction_s(project_name)

    if proj_data is None:
        abort(404)

    # make_svg_bat(proj_data['filename'], path)

    result = {'project': proj_data}

    return _my_format(EXTRACT.ROOT,result=result,code=200)

