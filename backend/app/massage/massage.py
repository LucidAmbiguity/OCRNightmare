""" Massage PDF text data in to a json object

    Copyright © 2021 - All Rights Reserved - Lucid Ambiguity
"""

from app.types.my_types import XtracDoc



from app.types.my_types import MyArgs
from .extract_text_from_pdf import gettext_all
from .extract_text_from_pdf_random import gettext_all_random
# from app.dothething import gettext
# from app.random_data import gettext_random




def extract_data_all(filename:str)-> list[XtracDoc]:

    my_args = MyArgs(
        input = filename,
        output = filename+'.text',
        password= '',
        pages = '1-N',
        convert_white = True,
        noligatures = True,
        extra_spaces = True,
        mode = 'layout',
        grid = 3,
        fontsize = 3,
        noformfeed = False,
        skip_empty = False
    )

    return gettext_all(my_args)


def extract_data_all_random(filename:str)->list[XtracDoc]:

    my_args =  MyArgs(
        input = filename,
        output = filename+'.text',
        password= '',
        pages = '1-N',
        convert_white = True,
        noligatures = True,
        extra_spaces = True,
        mode = 'layout',
        grid = 3,
        fontsize = 3,
        noformfeed = False,
        skip_empty = False,
    )
    return gettext_all_random(my_args)
