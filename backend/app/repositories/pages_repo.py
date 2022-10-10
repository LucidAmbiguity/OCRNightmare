"""A Page Repository"""
# Possibly unneeded be this small repo
# However its good practice for untangling the rest of the app

from app.models import (
    page_schema,
    pages_schema,
)
# from app.ocrnightmare.helpers.my_types import PageT
from app.interfaces.db_page_if import DBPageI

from typing import TYPE_CHECKING, Optional, Type


if TYPE_CHECKING:
    from app.models import Page
    from app.types import PageT


class PagesRepo:
    """A Page Repository"""

    _page_db: Optional['Page'] = None


    def __init__(
            self,
            db_page_i:Type[DBPageI]=DBPageI,
            ) ->None:

        self._db_page_i = db_page_i()


    def _return_logic(self,page_db:Optional['Page'])->Optional['PageT']:
        if page_db is None:
            return None
        page_: 'PageT' = page_schema.dump(page_db)
        return page_


    # def new_page(self,new_page_t:'NewPageTup')->Optional['PageT']:
    #     page_db = self._db_page_i.new_page(new_page_t)
    #     return self._return_logic(page_db)

    def get_all_pages(self)->list[Optional['PageT']]:
        pages_db: list['Page'] = self._db_page_i.get_all_pages()
        pages_: list[Optional['PageT']] = pages_schema.dump(pages_db)
        return pages_ # type: ignore[misc]

    def get_page_by_id(self, id:Optional[int])->Optional['PageT']:  # pylint: disable=redefined-builtin invalid-name
        page = self._db_page_i.get_by_id(id)
        return self._return_logic(page)

