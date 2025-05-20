#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fileinput
import sys
import re
# This script converts a markdown table to HTML
# so that rowspan can be used

# options: -d for debug -h for html output

# Usage: python3 table.py < input.txt > output.hmd
# This script reads a markdown table from input.txt and converts it to HTML


def iswhitespace(l):    # check if line is whitespace 
    l = l.strip()
    if l.startswith('#'):
        return True
    if len(l) == 0:
        return True
    return False
    
def td(col, firstcol=False):
    if firstcol:
        cs = rowspan(col)
        if cs:
            return(f'<td {cs}>{col}</td>')
    return f'<td>{col}</td>'

def tr(cols, rs=False):
    row = f"<tr>"
    firstcol = True
    bold = True
    for col in cols:
        # if the first column is empty, it must be part of a rowspan so skip it
        if firstcol and len(col.strip()) == 0:
            pass
        else: 
            if bold and not rs:
                col = f"<b>{col}</b>"  
            row += td(col.strip(), firstcol)
        firstcol = False
        bold = not bold
 
    row += "</tr>"
    return row


def rowspan(c):
    # extract html comment from the first column
    m = re.search(r'<!---(.*?)--->', c)
    if m:
        return m.group(1).strip()   
    else:
        return None

# read all the lines
lines = list(fileinput.input(inplace=False))
debug = False
previous_line = ""
i = 0
for line in lines:
    line = line.rstrip()
    cols = line.split('|')

    if len(cols) >= 2:
        cols.pop(0)
        cols.pop(-1)   
    
        if iswhitespace(previous_line):
            print(f"<table>")

        if len(cols) == 7:  # relative sizes
            print(tr(cols, rs=True))
        else:
            print(tr(cols))

        next_line = lines[i + 1] if i + 1 < len(lines) else ''

        if iswhitespace(next_line):
            print(r'</table>')
    else:
        print(lines[i].strip())
    previous_line = line
    i += 1


