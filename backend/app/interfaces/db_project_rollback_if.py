
import shutil
from typing import cast
from app.extensions import db
from app.types.my_types import ProjectT
from app.models import Project
from app.models.models import Page, TextLine

class DBProjRollbackInterface():
    """
        DBInterface to the Db and helper methods
        hide dependencies or something
    """

    def del_proj_by_name(self, p_name:str)->bool:
        project_db = cast( ProjectT, Project.query.filter_by(name=p_name).first()) # type: ignore[misc]
        print(project_db)
        if project_db.status == 0:
            shutil.rmtree(f'instance/data/{p_name}')

            db.session.delete(project_db)
            db.session.commit()
            return True
        return False

    def rollback_from_1(self, p_name:str)->bool:
        project_db = cast( ProjectT, Project.query.filter_by(name=p_name).first()) # type: ignore[misc]
        pages = cast(list[Page],project_db.pages.all())
        if project_db.status == 1:
            for page in pages:
                text_lines = cast(list[TextLine],page.text_lines.all())
                for t_line in text_lines:
                    chars = t_line.chars.all()
                    for ch in chars:
                        db.session.delete(ch)
                    db.session.delete(t_line) # type: ignore[misc]
                db.session.delete(page)
            project_db.status = 0
            db.session.commit() # type: ignore[misc]
            return True
        return False


