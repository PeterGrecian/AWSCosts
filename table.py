#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fileinput
import sys
import re
# This script converts a markdown table to HTML

# options: -d for debug -h for html output

# Usage: python3 table.py < input.txt > output.hmd
# This script reads a markdown table from input.txt and converts it to HTML

options = sys.argv[1:]
if '-d' in options:
    debug = True
else:
    debug = False
if '-h' in options:
    html = True
else:
    html = False

# column styles
styles = ["font-weight: bold; width: 12%",
          "font-weight: width: 32%",
          "font-weight: bold; width: 8%; text-align:right",
          "font-weight; width: 52%"
] 
         
border = "border:1px solid #999;border-collapse: collapse; padding: 0.3%"
table = "width: 100%"

# for relative sizes table
rs_styles = ["width: 14%"] * 7

# if there is a rowspan in the first column the first cell must be omitted in subsequent rows
# easiest way to do this is to not put it in the input file

def iswhitespace(l):    # check if line is whitespace 
    l = l.strip()
    if l.startswith('#'):
        return True
    if len(l) == 0:
        return True
    return False
    
def td(col, style, firstcol=False):
    if firstcol:
        cs = rowspan(col)
        if cs:
            return(f'<td {cs} style="{style};{border}">{col}</td>')
    return f'<td style="{style};{border}">{col}</td>'

def tr(cols, styles, skip=False):
    row = f"<tr style='{border}'>"
    firstcol = True
    for col, style in zip(cols, styles):
        # if the first column is empty, it must be part of a rowspan so skip it
        if firstcol and len(col.strip()) == 0:
            pass
        else:   
            row += td(col.strip(), style, firstcol)
        firstcol = False
 
    row += "</tr>"
    return row


def rowspan(c):
    # extract html comment from the first column
    m = re.search(r'<!---(.*?)--->', c)
    if m:
        return m.group(1).strip()   
    else:
        return None

def say(msg):
    #debug = True
    #debug = False
    if debug:
        print(f"<!-- {msg} -->")

# read all the lines
lines = list(fileinput.input(inplace=False))
debug = False
previous_line = ""
i = 0
for line in lines:
    line = line.rstrip()

    say(f'{i + 1:2} {line}')

    cols = line.split('|')

    if len(cols) >= 2:
        cols.pop(0)
        cols.pop(-1)   
    
        if iswhitespace(previous_line):
            print(f"<table style='{table};{border}'>")

        if len(cols) == 7:  # relative sizes
            print(tr(cols, rs_styles))
        else:
            print(tr(cols, styles))

        next_line = lines[i + 1] if i + 1 < len(lines) else ''

        if iswhitespace(next_line):
            print(r'</table>')

    else:
        if not html:
            print(lines[i].strip())
    previous_line = line
    i += 1


