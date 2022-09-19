""" ocrnightmare projects route Controller """

from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.projects import projects_bp # pylint: disable=import-self
from .._my_format import _my_format

@projects_bp.route('/', methods=['GET', 'POST'])
@projects_bp.route('', methods=['GET', 'POST'])
def projects_root():
    """Root route of ocrnightmare projects Module"""


    return _my_format(OCRN.Projects,code=200)
