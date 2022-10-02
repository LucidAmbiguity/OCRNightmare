"""Model Unit TEST FILE"""
# pylint: disable=invalid-name


from unittest.mock import patch
from app.models import Character

from tests.helpers import attr_counter


def test_character_has_expected_attributes():
    """test Character() has expected attributes"""
    character = Character()
    assert hasattr(character,'id')
    assert hasattr(character,'text_line_id')
    assert hasattr(character,'char')
    assert hasattr(character,'width')
    assert hasattr(character,'x0')
    assert hasattr(character,'y0')
    assert hasattr(character,'x1')
    assert hasattr(character,'y1')
    assert hasattr(character,'text_line')
    # query can only be checked within an app context the others come
    # with sqlalchemy
    # those above are user defined
    ## attr_counter counts query however looking at
    ## it triggers deep sql-alchemy code
    # assert hasattr(character,'query')
    assert hasattr(character,'metadata')
    assert hasattr(character,'query_class')
    assert hasattr(character,'registry')
    attr_count = attr_counter(character)
    assert attr_count == 13  # count check will fail if attributes added to model.  # pylint: disable=line-too-long
