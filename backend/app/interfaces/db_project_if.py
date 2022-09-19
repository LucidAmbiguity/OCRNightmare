""" DB Project Interface Thingy """


# from app.types import NewProjTup
# from app.extensions import db
from typing import Optional
from app.models import  Project


class DBProjI:
    """ Proj Interface """

    def get_all(self)->Optional[list[Project]]:
        result: Optional[list[Project]] = Project.query.all()  # type: ignore[misc]
        return result