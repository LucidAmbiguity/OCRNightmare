"""Model Unit TEST FILE"""
# pylint: disable=invalid-name


from unittest.mock import patch
from app.models import Page, page_schema, pages_schema
from app.interfaces.db_page_if import DBPageI
from app.types.my_types import NewPageTup

from tests.helpers import attr_counter


def test_page_has_expected_attributes():
    """test Page() has expected attributes"""
    page = Page()
    assert hasattr(page,'id')
    assert hasattr(page,'project_id')
    assert hasattr(page,'project')
    # query can only be checked within an app context the others come
    # with sqlalchemy
    # those above are user defined
    ## attr_counter counts query however looking at
    ## it triggers deep sql-alchemy code
    # assert hasattr(page,'query')
    assert hasattr(page,'metadata')
    assert hasattr(page,'query_class')
    assert hasattr(page,'registry')
    attr_count = attr_counter(page)
    assert attr_count == 7  # count check will fail if attributes added to model.  # pylint: disable=line-too-long


@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def test_page_interface_returns_Page(a,b,c): # pylint: disable=unused-argument
    project_id = 1
    new_page_tuple = NewPageTup(project_id)
    new_page = DBPageI().new_page(new_page_tuple)
    assert new_page.project_id == project_id
    assert isinstance(new_page,Page)


def test_page_schema(new_page_1):
    """test text line schema"""

    assert page_schema.dump(new_page_1) == {'id': 1, 'project_id': 1}

def test_pages_schema(new_page_1,new_page_2):
    """test text lines schema"""
     # pylint: disable=line-too-long
    pages = [new_page_1,new_page_2]
    print(pages)
    assert pages_schema.dump(pages) == [
      {'id': 1, 'project_id': 1},
      {'id': 2, 'project_id': 1},
    ]
