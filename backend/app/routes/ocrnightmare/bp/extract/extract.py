""" ocrnightmare extract route Controller """

from flask import abort
from typing import TYPE_CHECKING

from app.routes.ocrnightmare.bp.extract import extract_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.constants.OCRN import OCRN

from app.services.extraction_s import extraction_s,random_extraction_s
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

    result = {'project': proj_data}

    return _my_format(EXTRACT.ROOT,result=result,code=200)


# # This route for use in creating Test data from Real data
# # for use in Later tests and discussions. without compromising
# # The original data. Simple random replacement of letters and numbers
# # only relation back being it was a letter or was a number.
@extract_bp.route('', methods=['POST'])
def extract_random(project_name:str)->'Response':
    """Extract raw data from supplied PDF"""

    proj_data = random_extraction_s(project_name)

    if proj_data is None:
        abort(404)

    result = {'project': proj_data}

    return _my_format(EXTRACT.ROOT,result=result,code=200)

