""" ocrnightmare BluePrint Module """
from flask import Blueprint
ocrnightmare = Blueprint("ocrnightmare", __name__,)
from .ocrnightmare import ocrnightmare # pylint: disable=wrong-import-position
