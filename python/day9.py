#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

def computeMarker(markerValue, next):
    print ""

with open("day9.txt") as f:
    content = f.read()
    for c,i in enumerate(content):
        markerStart = 0
        marker = ""
        if c == '(' or len(marker) > 0:
            markerStart = i
            marker += c
        elif c == ')':
            x = int(markerValue.remove('(').remove(')').split('x')[0]) # repeat
            y = int(markerValue.remove('(').remove(')').split('x')[1]) # char size
            nc = content[i:i+x]
            markerValue = c * y
