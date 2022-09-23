""" Modified Fitz CLI

    Extract all characters from a pdf and their coordinates
    on the page.
    arrange into text lines and pages
    the returns XtracDoc = tuple[PageWBB,tuple[width,height]]
    WBB : with bounding box
    also has

    I/O Side EFFECT: creates a project_name.txt file in
    'instance/data/<proj_name>'
    next to the original pdf

"""

# TODO make the text output a trigger

from .massage import extract_data_all,extract_data_all_random

