"""A Project Repository"""


# from app.models import project_schema
from app.interfaces.db_project_if import DBProjI

from typing import TYPE_CHECKING, Type
from app.types.my_types import ProjDataT


if TYPE_CHECKING:
    from app.models import Project


class ProjectsRepo:
    """A Project Repository"""

    def __init__(
            self,
            db_proj_i:Type[DBProjI]=DBProjI,
            ) ->None:

        self._db_proj_i = db_proj_i()



    def get_all_projects(self)->list['ProjDataT']:
        projects_all = self._db_proj_i.get_all()

        project_list = [ProjDataT(
             id=project.id,
             name=project.name,
             status=project.status,
             filename=project.filename,
             pages=project.pages.count(),
             customers=project.customers.count(),
        )
            for project in projects_all
        ]

        return project_list

