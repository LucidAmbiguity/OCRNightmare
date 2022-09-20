""" ocrnightmare projects route Controller """


from typing import TYPE_CHECKING
from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.projects import projects_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.repositories.projects_repo import ProjectsRepo
from .._my_format import _my_format


if TYPE_CHECKING:
    from flask import Response

@projects_bp.route('', methods=['GET', 'POST']) # type: ignore[misc, attr-defined]
def show()->'Response':
    """Root route of ocrnightmare projects Module"""
    project_list = ProjectsRepo().get_all_projects()

    result = {'projects': project_list}
    return _my_format(OCRN.Projects, result=result ,code=200  )
