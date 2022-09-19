""" ocrnightmare BluePrint Module """
from flask import Blueprint
ocrnightmare = Blueprint("ocrnightmare", __name__,)
from .ocrnightmare import ocrnightmare # type: ignore[misc] # pylint: disable=wrong-import-position
