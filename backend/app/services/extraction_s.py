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
from app.massage import extract_data_all,make_svg_bat,extract_data_all_random
from app.repositories import ProjectRepo
from app.types.my_types import ProjDataT


def extraction_s(proj_name:str)->ProjDataT:
    p_repo = ProjectRepo(proj_name)
    filename = p_repo.filename
    path = f'instance/data/{proj_name}'
    orig_file_location = f'{path}/{filename}'

    captured = extract_data_all(orig_file_location)
    is_saved = p_repo.save_extracted(captured)
    make_svg_bat.make_svg_bat(filename, path)
    return is_saved

def random_extraction_s(proj_name:str)->ProjDataT:
    p_repo = ProjectRepo(proj_name)
    filename = p_repo.filename
    path = f'instance/data/{proj_name}'
    orig_file_location = f'{path}/{filename}'

    captured = extract_data_all_random(orig_file_location)
    is_saved = p_repo.save_extracted(captured)
    make_svg_bat.make_svg_bat(filename, path)
    return is_saved
