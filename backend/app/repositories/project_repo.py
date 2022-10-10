"""A Project Repository"""


from app.interfaces.db_project_if import DBProjI
from app.interfaces.db_project_save_extraction_if import DBProjSaveExtractionI

from typing import TYPE_CHECKING, Type

from app.types.my_types import ProjDataT
from app.models import text_lines_schema,pages_schema,page_schema


if TYPE_CHECKING:
    from app.models import Project,Page
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

    def get_all_text_lines(self):
        pages:list['Page'] = self._project_db.pages.all()
        text_lines = []
        for page in pages:
            lines = page.text_lines.all()

            text_lines += lines
        t_ls = text_lines_schema.dump(text_lines)
        return t_ls

    def get_all_pages(self):
        pages:list['Page'] = self._project_db.pages.all()
        result = pages_schema.dump(pages)

        return result

    def get_page(self,page_id:int):
        page:'Page'= self._project_db.pages.filter_by(id=page_id).first()

        if page is None:
            return None
        result = page_schema.dump(page)

        return result

    def get_page_w_text(self,page_id:int):
        page:'Page'= self._project_db.pages.filter_by(id=page_id).first()

        if page is None:
            return None
        text_lines = page.text_lines.all()
        t_ls = text_lines_schema.dump(text_lines)
        p_sch = page_schema.dump(page)
        p_sch['text_lines'] = t_ls


        return p_sch


