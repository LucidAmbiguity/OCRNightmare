""" ocrnightmare pages BluePrint Module """


from flask import Blueprint
pages_bp = Blueprint("pages", __name__,)
from .pages_bp import pages_bp #type: ignore[misc] # pylint: disable=wrong-import-position
