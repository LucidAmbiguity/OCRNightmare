""" DB Page Interface Thingy """


from typing import Optional, cast
from app.types.my_types import NewPageTup
from app.extensions import db
from app.models import  Page


class DBPageI:
    """ Page Interface """

    def get_all(self)->list[Page]:
        result: list[Page] = Page.query.all()  # type: ignore[misc]
        return result

    def new_page(self,new_page:NewPageTup)->Page:

        new_page_db = Page(
                project_id = new_page.project_id,
        )

        db.session.add(new_page_db) # type: ignore[misc] # pylint: disable=no-member
        db.session.commit() # type: ignore[misc] # pylint: disable=no-member
        db.session.refresh(new_page_db) # type: ignore[misc]
        return new_page_db


    def get_page_by_id(self, uid:Optional[int])->Optional[Page]:
        return cast( Page, Page.query.filter_by(id=uid).first()) # type: ignore[misc]


