"""this file began as a lift from the fitz  module source code.
My intension is to capture some intermediate data
to be used in the verify/correct  OCR capture UI

this has been tweaked to return randomized data.

import argparse"""
# pylint: skip-file

#for Type Hinting
from io import BufferedWriter
from typing import Dict, List, Set, cast
from app.types.my_types import CharWBB, MyArgs, PageWBB, StrWBB, XtracDoc


# for Module
import bisect
import os
import sys
import statistics
import random

import fitz
from fitz.fitz import (
    TEXT_INHIBIT_SPACES,
    TEXT_PRESERVE_LIGATURES,
    TEXT_PRESERVE_WHITESPACE,
)




def get_list(rlist: str, limit:int, what: str="page")->list[int]:
    """Transform a page / xref specification into a list of integers.

    Args
    ----
        rlist: (str) the specification
        limit: maximum number, i.e. number of pages, number of objects
        what: a string to be used in error messages
    Returns
    -------
        A list of integers representing the specification.
    """
    N = str(limit - 1)
    rlist = rlist.replace("N", N).replace(" ", "")
    rlist_arr = rlist.split(",")
    out_list = []
    for seq, item in enumerate(rlist_arr):
        n = seq + 1
        if item.isdecimal():  # a single integer
            i = int(item)
            if 1 <= i < limit:
                out_list.append(int(item))
            else:
                sys.exit("bad %s specification at item %i" % (what, n))
            continue
        try:  # this must be a range now, and all of the following must work:
            i1c, i2c = item.split("-")  # will fail if not 2 items produced
            i1 = int(i1c)  # will fail on non-integers
            i2 = int(i2c)
        except:
            sys.exit("bad %s range specification at item %i" % (what, n))

        if not (1 <= i1 < limit and 1 <= i2 < limit):
            sys.exit("bad %s range specification at item %i" % (what, n))

        if i1 == i2:  # just in case: a range of equal numbers
            out_list.append(i1)
            continue

        if i1 < i2:  # first less than second
            out_list += list(range(i1, i2 + 1))
        else:  # first larger than second
            out_list += list(range(i1, i2 - 1, -1))

    return out_list

def open_file(filename: str, password: str, show: bool=False, pdf: bool=True)->fitz.Document:
    """Open and authenticate a document."""
    doc = cast(fitz.Document, fitz.open(filename)) # type: ignore[misc]
    if not doc.is_pdf and pdf is True: # type: ignore[misc]
        sys.exit("this command supports PDF files only")
    rc = -1
    if not doc.needs_pass: # type: ignore[misc]
        return doc # type: ignore[misc]
    if password:
        rc = doc.authenticate(password) # type: ignore[misc]
        if not rc:
            sys.exit("authentication unsuccessful")
        if show is True:
            print("authenticated as %s" % "owner" if rc > 2 else "user")
    else:
        sys.exit("'%s' requires a password" % doc.name) # type: ignore[misc]
    return doc # type: ignore[misc]

def page_layout(page:fitz.Page, textout:BufferedWriter, GRID:int, fontsize:int, noformfeed:bool, skip_empty:bool, flags:int) -> PageWBB:
    eop = b"\n" if noformfeed else bytes([12])

    # --------------------------------------------------------------------
    def find_line_index(values: list[int], value: float) -> int:
        """Find the right row coordinate.

        Args:
            values: (list) y-coordinates of rows.
            value: (int) lookup for this value (y-origin of char).
        Returns:
            y-ccordinate of appropriate line for value.
        """
        i = bisect.bisect_right(values, value)
        if i:
            return values[i - 1]
        raise RuntimeError("Line for %g not found in %s" % (value, values))

    # --------------------------------------------------------------------
    def curate_rows(rows: Set[int], GRID: int) -> list[int]:
        rows_list:list[int] = list(rows)
        rows_list.sort()  # sort ascending
        nrows = [rows_list[0]]
        for h in rows_list[1:]:
            if h >= nrows[-1] + GRID:  # only keep significant differences
                nrows.append(h)
        return nrows  # curated list of line bottom coordinates

    def my_randomizer(ch:str)->str:
        temp = ch
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number ='0123456789'
        if ch in lower:
            temp=random.choice(lower)
        if ch in upper:
            temp=random.choice(upper)
        if ch in number:
            temp=random.choice(number)
        return temp


    def process_blocks(blocks: List[Dict], page: fitz.Page)-> tuple[list[CharWBB],set[int],float,float,float]:
        rows: set[int] = set() # type: ignore[misc]
        page_width: float = page.rect.width # type: ignore[misc]
        page_height: float = page.rect.height # type: ignore[misc]
        rowheight = page_height
        left = page_width
        right:float = 0
        chars : List[CharWBB] = []
        for block in blocks: # type: ignore[misc]
            for line in block["lines"]: # type: ignore[misc]
                if line["dir"] != (1, 0):  # type: ignore[misc] # ignore non-horizontal text
                    continue
                x0, y0, x1, y1 = line["bbox"] # type: ignore[misc]
                if y1 < 0 or y0 > page.rect.height:  # ignore if outside CropBox
                    continue
                # upd row height
                height = y1 - y0

                if rowheight > height:
                    rowheight = height
                for span in line["spans"]:
                    if span["size"] <= fontsize:
                        continue
                    for c in span["chars"]:
                        x0, y0, x1, y1 = c["bbox"]
                        cwidth = x1 - x0
                        ox, oy = c["origin"]
                        oy = int(round(oy))
                        rows.add(oy)
                        ch = c["c"]
                        if left > ox and ch != " ":
                            left = ox  # update left coordinate
                        if right < x1:
                            right = x1  # update right coordinate
                        # handle ligatures:
                        if cwidth == 0 and chars != []:  # potential ligature
                            old_ch, old_ox, old_oy, old_cwidth, old_x0, old_y0, old_x1, old_y1 = chars[-1]
                            if old_oy == oy:  # ligature
                                if old_ch != chr(0xFB00):  # previous "ff" char lig?
                                    lig = joinligature(old_ch + ch)  # no
                                # convert to one of the 3-char ligatures:
                                elif ch == "i":
                                    lig = chr(0xFB03)  # "ffi"
                                elif ch == "l":
                                    lig = chr(0xFB04)  # "ffl"
                                else:  # something wrong, leave old char in place
                                    lig = old_ch
                                chars[-1] = (lig, old_ox, old_oy, old_cwidth, old_x0, old_y0, old_x1, old_y1)
                                continue
                        ch = my_randomizer(ch)
                        chars.append((ch, ox, y1, cwidth, x0, y0, x1, y1))  # all chars on page

        return chars, rows, left, right, rowheight

    def joinligature(lig: str) -> str:
        """Return ligature character for a given pair / triple of characters.

        Args:
            lig: (str) 2/3 characters, e.g. "ff"
        Returns:
            Ligature, e.g. "ff" -> chr(0xFB00)
        """

        if lig == "ff":
            return chr(0xFB00)
        elif lig == "fi":
            return chr(0xFB01)
        elif lig == "fl":
            return chr(0xFB02)
        elif lig == "ffi":
            return chr(0xFB03)
        elif lig == "ffl":
            return chr(0xFB04)
        elif lig == "ft":
            return chr(0xFB05)
        elif lig == "st":
            return chr(0xFB06)
        return lig

    # --------------------------------------------------------------------
    def make_textline(left:float, slot:float, minslot:float, lchars:list[CharWBB])->str:
        """Produce the text of one output line.

        Args:
            left: (float) left most coordinate used on page
            slot: (float) avg width of one character in any font in use.
            minslot: (float) min width for the characters in this line.
            chars: (list[tuple]) characters of this line.
        Returns:
            text: (str) text string for this line
        """
        text = ""  # we output this
        old_char = ""
        old_x1:float = 0  # end coordinate of last char
        old_ox:float = 0  # x-origin of last char
        if minslot <= fitz.EPSILON:
            raise RuntimeError(
                "program error: minslot too small = %g" % minslot)

        for c in lchars:  # loop over characters
            char, ox, _, cwidth, *rest = c
            ox = ox - left  # its (relative) start coordinate
            x1 = ox + cwidth  # ending coordinate

            # eliminate overprint effect
            if old_char == char and ox - old_ox <= cwidth * 0.2:
                continue

            # omit spaces overlapping previous char
            if char == " " and (old_x1 - ox) / cwidth > 0.8:
                continue

            old_char = char
            # close enough to previous?
            if ox < old_x1 + minslot:  # assume char adjacent to previous
                text += char  # append to output
                old_x1 = x1  # new end coord
                old_ox = ox  # new origin.x
                continue

            # else next char starts after some gap:
            # fill in right number of spaces, so char is positioned
            # in the right slot of the line
            if char == " ":  # rest relevant for non-space only
                continue
            delta = int(ox / slot) - len(text)
            if ox > old_x1 and delta > 1:
                text += " " * delta
            # now append char
            text += char
            old_x1 = x1  # new end coordinate
            old_ox = ox  # new origin
        return text.rstrip()

    captured: list[StrWBB] = []
    # extract page text by single characters ("rawdict")
    blocks = page.get_text("rawdict", flags=flags)["blocks"]
    chars, rows_set, left, right, rowheight = process_blocks(blocks, page)
    # captured += [(blocks,chars, list(rows), left, right, rowheight)]
    if chars == []:
        if not skip_empty:
            textout.write(eop)  # write formfeed
        return # type: ignore[return-value]
    # compute list of line coordinates - ignoring small (GRID) differences
    rows = curate_rows(rows_set, GRID)
    # [385,260,135,405,406,281,156,291,166,301,302,177,187,322,323,198,73,333,208,83,84,218,219,354,104,364,365,239,115,374,375,250,125]

    # sort all chars by x-coordinates, so every line will receive char info,
    # sorted from left to right.
    chars.sort(key=lambda c: c[1])
    # captured += [( list(rows), left, right, rowheight)]


    # populate the lines with their char info
    lines:dict[int,list[CharWBB]] = {}  # key: y1-ccordinate, value: char list
    for c in chars:
        _, _, oy, *_ = c
        y = find_line_index(rows, oy)  # y-coord of the right line
        lchars = lines.get(y, [])  # read line chars so far
        lchars.append(c)  # append this char
        lines[y] = lchars  # write back to line

    # ensure line coordinates are ascending
    keys = list(lines.keys())
    keys.sort()

    # -------------------------------------------------------------------------
    # Compute "char resolution" for the page: the char width corresponding to
    # 1 text char position on output - call it 'slot'.
    # For each line, compute median of its char widths. The minimum across all
    # lines is 'slot'.
    # The minimum char width of each line is used to determine if spaces must
    # be inserted in between two characters.
    # -------------------------------------------------------------------------
    slot = right - left
    minslots:dict[int,float] = {}
    for k in keys:
        lchars = lines[k]
        ccount = len(lchars)
        if ccount < 2:
            minslots[k] = 1
            continue
        widths = [c[3] for c in lchars]
        widths.sort()
        this_slot = statistics.median(widths)  # take median value
        if this_slot < slot:
            slot = this_slot
        minslots[k] = widths[0]

    # compute line advance in text output
    rowheight = rowheight * (rows[-1] - rows[0]) / \
        (rowheight * len(rows)) * 1.2
    rowpos:float = rows[0]  # first line positioned here
    textout.write(b"\n")
    for k in keys:  # walk through the lines
        while rowpos < k:  # honor distance between lines
            textout.write(b"\n")
            rowpos += rowheight
        text = make_textline(left, slot, minslots[k], lines[k])
        captured += [(text,lines[k])] # list[CharWBB]
        textout.write((text + "\n").encode("utf8", errors="surrogatepass"))
        rowpos = k + rowheight

    textout.write(eop)  # write formfeed
    return captured

# def gettext_random(args:MyArgs)->XtracDoc:
#     doc = open_file(args.input, args.password, pdf=False)
#     pagel = get_list(args.pages, doc.page_count + 1)
#     output = args.output
#     if output == None:
#         filename, _ = os.path.splitext(doc.name)
#         output = filename + ".txt"
#     textout = open(output, "wb")
#     flags = TEXT_PRESERVE_LIGATURES | TEXT_PRESERVE_WHITESPACE
#     if args.convert_white:
#         flags ^= TEXT_PRESERVE_WHITESPACE
#     if args.noligatures:
#         flags ^= TEXT_PRESERVE_LIGATURES
#     if args.extra_spaces:
#         flags ^= TEXT_INHIBIT_SPACES
#     func = {

#         "layout": page_layout,
#     }
#     captured_all = []
#     for pno in pagel:
#         page = doc[pno - 1]
#         captured_all += func[args.mode](
#             page,
#             textout,
#             args.grid,
#             args.fontsize,
#             args.noformfeed,
#             args.skip_empty,
#             flags=flags,
#         )

#     textout.close()
#     return (captured_all,(doc[0].rect.width,doc[0].rect.height))


def gettext_all_random(args:MyArgs)->list[XtracDoc]:
    doc = open_file(args.input, args.password, pdf=False)
    pagel = get_list(args.pages, doc.page_count + 1)
    output = args.output
    if output == None:
        filename, _ = os.path.splitext(doc.name)
        output = filename + ".txt"
    textout = open(output, "wb")
    flags = TEXT_PRESERVE_LIGATURES | TEXT_PRESERVE_WHITESPACE
    if args.convert_white:
        flags ^= TEXT_PRESERVE_WHITESPACE
    if args.noligatures:
        flags ^= TEXT_PRESERVE_LIGATURES
    if args.extra_spaces:
        flags ^= TEXT_INHIBIT_SPACES
    # func = {

    #     "layout": page_layout,
    # }
    captured_all:list[XtracDoc] = []
    for pno in pagel:
        page = doc[pno - 1]
        captured_all.append((page_layout(
            page,
            textout,
            args.grid,
            args.fontsize,
            args.noformfeed,
            args.skip_empty,
            flags=flags,
        ),(doc[pno-1].rect.width,doc[pno-1].rect.height)))
    textout.close()

    return captured_all
# PageWBB
