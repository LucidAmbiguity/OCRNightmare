""" ocrnightmare extract BluePrint Module """


from flask import Blueprint
extract_bp = Blueprint("extract", __name__,)
from .extract import extract_bp #type: ignore[misc] # pylint: disable=wrong-import-position
