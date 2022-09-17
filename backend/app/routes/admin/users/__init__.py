""" admin users BluePrint Module """
from flask import Blueprint
users = Blueprint("users", __name__,)
from .users import users #type: ignore[misc] # pylint: disable=wrong-import-position
