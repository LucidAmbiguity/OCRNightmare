"""A Project Repository"""


# from app.models import project_schema
from app.interfaces.db_project_if import DBProjI

from typing import TYPE_CHECKING, Optional, Type
from app.types.my_types import ProjDataT


if TYPE_CHECKING:
    from app.models import Project
    from app.types.my_types import NewProjTup


class ProjectsRepo:
    """A Project Repository"""

    def __init__(
            self,
            db_proj_i:Type[DBProjI]=DBProjI,
            ) ->None:

        self._db_proj_i = db_proj_i()

    def _return_logic(self,project:Optional['Project'])->Optional['ProjDataT']:
        if project is None:
            return None
        project_: 'ProjDataT' = ProjDataT(
             id=project.id,
             name=project.name,
             status=project.status,
             filename=project.filename,
             pages=project.pages.count(),
             customers=project.customers.count(),
        )
        return project_



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

    def get_project_by_name(self, name:Optional[str])->Optional['Project']:
        project = self._db_proj_i.get_project_by_name(name)
        return project


    def new_project(self,new_project:'NewProjTup')->Optional[ProjDataT]:
        _new_project = self._db_proj_i.new_project(new_project)

        return self._return_logic(_new_project)

