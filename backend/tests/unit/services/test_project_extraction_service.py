from unittest.mock import patch
from app.services.extraction_s import extraction_s
from app.interfaces.db_project_save_extraction_if import build_page
from app.models.models import Project
from app.types.my_types import XtracDoc,MockCount



class MockReturn1:
    id = 1
    name= 'filename'
    status = 0
    filename = 'filename.pdf'
    pages= MockCount(7)
    customers= MockCount(0)
    # def filter_by(self,*args,**Kwargs):
    #     return self
    # def first(self,*args,**Kwargs):
    #     return self
    # def first_or_404(self,*args,**Kwargs):
    #     return self
    def save_extracted(self,*args,**Kwargs):
        return True
class MockReturn2:
    id = 1
    name= 'filename'
    status = 1
    filename = 'filename.pdf'
    pages= MockCount(7)
    customers= MockCount(0)
    # def filter_by(self,*args,**Kwargs):
    #     return self
    # def first(self,*args,**Kwargs):
    #     return self
    # def first_or_404(self,*args,**Kwargs):
    #     return self
    def save_extracted(self,*args,**Kwargs):
        return True

mock_return = MockReturn1()
mock_return_2 = MockReturn2()



xtract_doc: XtracDoc = ([('ab',[('a', 1.2, 2.3, 3.4, 4.4, 2.3, 3.4, 4.4),
('b', 1.2, 2.3, 3.4, 4.4, 2.3, 3.4, 4.4)]),
('cd',[('c', 1.2, 2.3, 3.4, 4.4, 2.3, 3.4, 4.4),
('d', 1.2, 2.3, 3.4, 4.4, 2.3, 3.4, 4.4)])],(8.5,11.3))

# @patch('flask_sqlalchemy._QueryProperty.__get__',return_value = mock_return)


@patch('app.services.extraction_s.make_svg_bat.make_svg_bat',return_value=None)
@patch('app.services.extraction_s.extract_data_all',return_value=xtract_doc)
@patch('app.services.extraction_s.ProjectRepo',return_value=mock_return)
def test_extraction_service(a,b,c):
    proj_name = mock_return.name

    result = extraction_s(proj_name)

    b.assert_called_with('instance/data/filename/filename.pdf')
    c.assert_called_with('filename.pdf', 'instance/data/filename')

    assert result is True


def test_build_page():
    project = Project()
    build_page(project,[xtract_doc,xtract_doc])
    print(project)
    print(project.pages)
    print(project.pages.count())
    print(project.pages.all()[0].text_lines.count())
    assert project.pages.count() == 2
    assert project.pages.all()[0].text_lines.count() == 2
    assert project.pages.all()[0].text_lines.all()[0].chars.count() == 2


@patch('app.services.extraction_s.make_svg_bat.make_svg_bat',return_value=None)
@patch('app.services.extraction_s.extract_data_all',return_value=xtract_doc)
@patch('app.services.extraction_s.ProjectRepo',return_value=mock_return_2)
def test_extraction_service_fails_if_not_status_0_(a,b,c):
    proj_name = mock_return.name

    result = extraction_s(proj_name)

    b.assert_not_called()
    c.assert_not_called()

    assert result is False