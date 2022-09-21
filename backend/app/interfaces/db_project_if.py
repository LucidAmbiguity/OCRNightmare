""" DB Project Interface Thingy """


from typing import Optional, cast
from app.types.my_types import NewProjTup
from app.extensions import db
from app.models import  Project


class DBProjI:
    """ Proj Interface """

    def get_all(self)->list[Project]:
        result: list[Project] = Project.query.all()  # type: ignore[misc]
        return result

    def get_project_by_name(self, name:Optional[str])->Optional[Project]:
        return cast( Project, Project.query.filter_by(name=name).first()) # type: ignore[misc]


    def new_project(self,new_project:NewProjTup)->Project:

        new_project_db = Project(
                name = new_project.name,
                status = new_project.status,
                filename = new_project.filename,
        )

        db.session.add(new_project_db) # type: ignore[misc] # pylint: disable=no-member
        db.session.commit() # type: ignore[misc] # pylint: disable=no-member
        db.session.refresh(new_project_db) # type: ignore[misc]
        return new_project_db
