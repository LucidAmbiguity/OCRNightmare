"""

    do the ugly loop of the captured extracted object to db.Models


 """


from app.models.models import Page, Project,Character, TextLine
from app.extensions import db


def build_page(project,captured):

    for pgn, captured_page in enumerate(captured):
        page = Page()
        page.page_num = pgn
        page.width = captured_page[1][0]
        page.height = captured_page[1][1]
        for line in captured_page[0]:
            text_line = TextLine()
            text_line.text_line = line[0]
            for char_array in line[1]:
                char = Character()
                char.char = char_array[0]
                char.width = char_array[3]
                char.x0 = char_array[4]
                char.y0 = char_array[5]
                char.x1 = char_array[6]
                char.y1 = char_array[7]
                text_line.chars.append(char)
            page.text_lines.append(text_line)
        project.pages.append(page) #
    return project

class DBProjSaveExtractionI:
    """ Save Extraction DB Interface"""

    #!captured needs a type
    def save(self,project_name:str,captured)->bool:
        project: Project = Project.query.filter_by(name=project_name).first_or_404() # type: ignore[misc]

        build_page(project,captured)
        project.status = 1
        db.session.commit() # type: ignore[misc]  # pylint: disable=no-member
        return True

