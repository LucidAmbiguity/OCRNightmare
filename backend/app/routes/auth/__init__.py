"""Auth BluePrint Module"""
from flask import Blueprint

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

from .auth import auth #type: ignore[misc]# pylint: disable=wrong-import-position
