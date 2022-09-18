from app.routes.ocrnightmare import ocrnightmare # pylint: disable=import-self
from ._format import _my_format

from app.constants.OCRN import OCRN

@ocrnightmare.route('/', methods=['GET', 'POST'])
@ocrnightmare.route('', methods=['GET', 'POST'])
def ocrnightmare_root():
    """Root route of  ocrnightmare Module"""


    return _my_format(OCRN.ROOT,code=200)
