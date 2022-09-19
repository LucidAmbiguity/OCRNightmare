""" ocrnightmare projects BluePrint Module """


from flask import Blueprint
projects_bp = Blueprint("projects", __name__,)
from .projects_bp import projects_bp #type: ignore[misc] # pylint: disable=wrong-import-position
