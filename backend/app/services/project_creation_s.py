""" Project Creation Service"""

import os
from werkzeug.utils import secure_filename

# from app.logger import logger
from app.types.my_types import NewProjTup
from app.constants.OCRN import OCRN
from app.constants.other import PDF,OCR_BASE

from app.repositories.projects_repo import ProjectsRepo

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask import Flask
    from werkzeug.datastructures import FileStorage


class DiskService:
    """ AN IO Service"""

    def store_project(self,project_path:str,project_name:str,filename:str,req_file:'FileStorage')->bool:
        os.mkdir(os.path.join(project_path, 'data', project_name))
        req_file.save(os.path.join(
            project_path, 'data', project_name, filename
        ))
        return True

    def listdir(self,path:str)->list:
        return os.listdir(path)



class ProjectCreationSRV():
    """create a project service"""

    def __init__(self, current_app:'Flask',req_file:'FileStorage'):
        self._current_app = current_app
        self._req_file = req_file

    def _create(self, project_name:str, filename:str)->bool:
        new_project_tuple = NewProjTup(project_name, filename, 0)
        new_project = ProjectsRepo().new_project(new_project_tuple)

        if new_project is None:
            return False
        return True



    def create_project(self):
        filename = secure_filename(self._req_file.filename) # type: ignore[arg-type]
        project_name = filename[:PDF]
        project_path = self._current_app.instance_path
        dircontents = DiskService().listdir(OCR_BASE)
        # logger.info('%s, %s', filename, dircontents)

        if project_name in dircontents:
            return OCRN.FAILinDir

        existing_project = ProjectsRepo().get_project_by_name(project_name)
        if existing_project:
            # logger.info('FAIL proj_int is not None , %s', (proj_int is not None))
            return OCRN.FAILinDB

        is_stored = DiskService().store_project(project_path,project_name,filename,self._req_file)
        if not is_stored:
            return OCRN.FAILinDir

        is_created = self._create(project_name, filename)
        if not is_created:
            return OCRN.FAILinCreate

        return (OCRN.S_C_Proj_)[0]



