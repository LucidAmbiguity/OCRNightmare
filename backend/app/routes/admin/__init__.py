""" admin BluePrint Module """
from flask import Blueprint
admin = Blueprint("admin", __name__,)
from .admin import admin #type: ignore[misc]# pylint: disable=wrong-import-position
