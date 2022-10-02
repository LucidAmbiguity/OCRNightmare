"""Model Unit TEST FILE"""
# pylint: disable=invalid-name


from unittest.mock import patch
from app.models import TextLine

from tests.helpers import attr_counter


def test_text_line_has_expected_attributes():
    """test TextLine() has expected attributes"""
    text_line = TextLine()
    assert hasattr(text_line,'id')
    assert hasattr(text_line,'page_id')
    assert hasattr(text_line,'text_line')
    assert hasattr(text_line,'chars')
    assert hasattr(text_line,'page')
    # query can only be checked within an app context the others come
    # with sqlalchemy
    # those above are user defined
    ## attr_counter counts query however looking at
    ## it triggers deep sql-alchemy code
    # assert hasattr(text_line,'query')
    assert hasattr(text_line,'metadata')
    assert hasattr(text_line,'query_class')
    assert hasattr(text_line,'registry')
    attr_count = attr_counter(text_line)
    assert attr_count == 9  # count check will fail if attributes added to model.  # pylint: disable=line-too-long
