"""A Project Repository"""


from app.interfaces.db_project_if import DBProjI
from app.interfaces.db_project_save_extraction_if import DBProjSaveExtractionI

from typing import TYPE_CHECKING, Type

from app.types.my_types import ProjDataT


if TYPE_CHECKING:
    from app.models import Project
    from app.types import ProjectT


class ProjectRepo:
    """A Project Repository"""
    exists = False

    def __init__(
            self,
            project_name:str=None,

            db_p_i:Type[DBProjI]=DBProjI,
            db_p_s_e_i:Type[DBProjSaveExtractionI]=DBProjSaveExtractionI,
            ) ->None:

        self._db_p_i = db_p_i()
        self._db_p_s_e_i = db_p_s_e_i()

        self._project_db = self._db_p_i.get_by_name(project_name)
        if self._project_db is not None:
            self.id = self._project_db.id
            self.name = self._project_db.name
            self.status = self._project_db.status
            self.filename = self._project_db.filename
            self.pages = self._project_db.pages.count()
            self.customers = self._project_db.customers.count()
            self.exists = True

    def save_extracted(self, captured):
        is_saved = self._db_p_s_e_i.save(self.name,captured)
        return is_saved

    def get_data(self)->ProjDataT:
        return ProjDataT(
                id = self.id,
                name = self.name,
                status = self.status,
                filename = self.filename,
                pages = self.pages,
                customers = self.customers,
            )