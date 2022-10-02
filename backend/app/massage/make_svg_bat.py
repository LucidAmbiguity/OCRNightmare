"""Make SVG bat file
 This is process extracts the image from the PDF
 using Inkscape.exe
"""
import os
from typing import cast
import fitz
import sys

def get_inkscape_commands(
        num: int, curr_acct_pg_count:int, filename:str
    ) ->list[str]:

    out_file = filename #+'_out_'+str(num)+'.pdf'

    print('CREATING SVG Commands: ', file=sys.stderr)

    count=0
    inkscape = []
    for i in range(num,curr_acct_pg_count+1):  # pylint: disable=unused-variable
        count +=1
        inkfile = filename[:-3]+str(count-1)+'.svg'
        inkscape += [
                'inkscape --export-type=svg --export-filename=' +
                inkfile +
                ' --pdf-page='+str(count)+' '+out_file
            ]
    return inkscape


def make_svg_bat(filename: str, path: str)-> None:

    # print('in  splinter',filename,path)
    doc = cast(fitz.Document, fitz.open(os.path.join(path,filename)))  # type: ignore[misc] # pylint: disable=line-too-long
    pages = cast(int, doc.page_count)  # type: ignore[misc]
    inkscape = get_inkscape_commands(0,pages-1,filename)

    with open(os.path.join(path,'makeSvg.bat'), 'w', encoding='utf-8') as file_:
        for item in inkscape:
            file_.write(f'{item}\n')
            file_.write('if errorlevel 0 (   echo Success we move to the next %errorlevel% )\n\n')  # pylint: disable=line-too-long



