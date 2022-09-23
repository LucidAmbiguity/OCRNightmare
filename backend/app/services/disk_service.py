""" AN IO Service"""


import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
