""" Project Extraction Service

    Advance Project status to 1

        run the pdf file thru a modified Fitz cli program
        now a module called Rufus
            treated like a third party lib.
                does need some tweaking on returning spaces


        this returns a list[tuple[
                [list:of text lines with char bounding box],
                doc.width,
                doc.height
            ]]

        Extraction service will process this list of page tuples
        and submit to the project page repo for storage

        Will also call the MakeSvgService


"""

# from app.types.my_types import XtracDoc
from app.massage import extract_data_all
from app.repositories import ProjectRepo
from app.types.my_types import ProjDataT


def extraction_s(proj_name:str)->ProjDataT:
    p_repo = ProjectRepo(proj_name)
    filename = p_repo.filename
    orig_file_location = f'instance/data/{proj_name}/{filename}'

    captured = extract_data_all(orig_file_location)
    is_saved = p_repo.save_extracted(captured)
    return is_saved
