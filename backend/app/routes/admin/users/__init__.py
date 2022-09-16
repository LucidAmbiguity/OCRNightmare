""" admin users BluePrint Module """
from flask import Blueprint
users = Blueprint("users", __name__,)
from .users import users # pylint: disable=wrong-import-position
