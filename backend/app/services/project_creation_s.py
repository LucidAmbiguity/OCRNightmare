""" Project Creation Service"""

from werkzeug.utils import secure_filename

# from app.logger import logger
from app.types.my_types import NewProjTup
from app.constants.OCRN import OCRN
from app.constants.other import PDF,OCR_BASE

from app.repositories import ProjectsRepo
from .disk_service import DiskService
from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from flask import Flask
    from werkzeug.datastructures import FileStorage
    from app.types.my_types import ProjDataT


class ProjectCreationSRV():
    """create a project service"""

    def __init__(self, current_app:'Flask',req_file:'FileStorage'):
        self._current_app = current_app
        self._req_file = req_file


    def _create(self, project_name:str, filename:str)->Optional['ProjDataT']:
        new_project_tuple = NewProjTup(project_name, filename, 0)
        return ProjectsRepo().new_project(new_project_tuple)


    def create_project(self):
        filename = secure_filename(self._req_file.filename) # type: ignore[arg-type]
        project_name = filename[:PDF]
        project_path = self._current_app.instance_path
        dircontents = DiskService().listdir(OCR_BASE)
        # logger.info('%s, %s', filename, dircontents)

        if project_name in dircontents:
            return (OCRN.FAILinDir,None)

        existing_project = ProjectsRepo().get_project_by_name(project_name)
        if existing_project:
            # logger.info('FAIL proj_int is not None , %s', (proj_int is not None))
            return (OCRN.FAILinDB,None)

        is_stored = DiskService().store_project(project_path,project_name,filename,self._req_file)
        if not is_stored:
            return (OCRN.FAILinDir,None)

        new_project = self._create(project_name, filename)
        if new_project is None:
            return (OCRN.FAILinCreate,None)

        return (OCRN.S_C_Proj_,new_project)



