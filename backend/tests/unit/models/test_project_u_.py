"""Model Unit TEST FILE"""
# pylint: disable=invalid-name


from unittest.mock import patch
from app.models import Project, project_schema, projects_schema
from app.interfaces.db_project_if import DBProjI
from app.types.my_types import NewProjTup

from tests.helpers import attr_counter


def test_project_has_expected_attributes():
    """test Project() has expected attributes"""
    project = Project()
    assert hasattr(project,'id')
    assert hasattr(project,'name')
    assert hasattr(project,'filename')
    assert hasattr(project,'status')
    assert hasattr(project,'pages')
    assert hasattr(project,'customers')
    # query can only be checked within an app context the others come
    # with sqlalchemy
    # those above are user defined
    # assert hasattr(project,'query')
    assert hasattr(project,'metadata')
    assert hasattr(project,'query_class')
    assert hasattr(project,'registry')
    attr_count = attr_counter(project)
    assert attr_count == 10  #count check will fail if attributes added to model.  # pylint: disable=line-too-long


@patch('app.extensions.db.session.refresh', return_value = 'junk_value')
@patch('app.extensions.db.session.commit', return_value = 'junk_value')
@patch('app.extensions.db.session.add', return_value = 'junk_value')
def test_project_interface_returns_Project(a,b,c): # pylint: disable=unused-argument
    project_name, filename = 'filename', 'filename.pdf'
    new_project_tuple = NewProjTup(project_name, filename, 0)
    new_project = DBProjI().new_project(new_project_tuple)
    assert new_project.name == project_name
    assert isinstance(new_project,Project)

def test_project_schema(new_proj_1):
    """test text line schema"""

    assert project_schema.dump(new_proj_1) == {'filename': 'filename.pdf', 'id': 1, 'name': 'filename', 'status': 0}

def test_projects_schema(new_proj_1,new_proj_2):
    """test text lines schema"""
     # pylint: disable=line-too-long
    projects = [new_proj_1,new_proj_2]
    print(projects)
    assert projects_schema.dump(projects) == [
      {'filename': 'filename.pdf', 'id': 1, 'name': 'filename', 'status': 0},
      {'filename': 'proj210304.pdf', 'name': 'proj210304', 'id': 2, 'status': 1},
    ]
