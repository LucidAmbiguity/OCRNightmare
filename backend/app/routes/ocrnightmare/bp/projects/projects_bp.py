""" ocrnightmare projects route Controller """


from flask import request,current_app



from app.constants.OCRN import OCRN
from app.routes.ocrnightmare.bp.projects import projects_bp # type: ignore[no-redef] # pylint: disable=import-self
from app.repositories.projects_repo import ProjectsRepo
from app.forms import UploadFile

from typing import TYPE_CHECKING

from app.services.project_creation_s import ProjectCreationSRV
from ..._my_format import _my_format


if TYPE_CHECKING:
    from flask import Response

@projects_bp.route('', methods=['GET']) # type: ignore[misc, attr-defined]
def show()->'Response':
    """Root route of ocrnightmare projects Module"""
    project_list = ProjectsRepo().get_all_projects()

    result = {'projects': project_list}
    return _my_format(OCRN.Projects, result=result ,code=200  )


@projects_bp.route('', methods=['POST']) # type: ignore[attr-defined,misc] # pylint:disable=line-too-long
def store()->'Response':

    form = UploadFile()
    if not form.validate_on_submit(): # type: ignore[,misc]
        result = {'errors':form.upfile.errors}
        return _my_format(OCRN.FAILinForm, code=400, result=result)

    req_file = request.files['upfile']
    creation_code, new_project = ProjectCreationSRV(current_app,req_file).create_project()

    if creation_code == OCRN.FAILinDir:
        return _my_format(OCRN.FAILinDir,code=400)

    if creation_code == OCRN.FAILinDB:
        return _my_format(OCRN.FAILinDB,code=400)

    if creation_code == OCRN.FAILinCreate:
        return _my_format(OCRN.FAILinCreate,code=400)

    result = {'project':new_project}
    return _my_format(OCRN.S_C_Proj_,result=result, x=new_project['name'])
    # return _my_format(OCRN.S_C_Proj_,x='Wrong')

