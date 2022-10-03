""" ocrnightmare text_lines BluePrint Module """


from flask import Blueprint
text_lines_bp = Blueprint("text_lines", __name__,)
from .text_lines_bp import text_lines_bp #type: ignore[misc] # pylint: disable=wrong-import-position
