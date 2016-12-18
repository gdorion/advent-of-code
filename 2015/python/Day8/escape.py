#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import re
memoryCount = 0

def replace_hex(input):
    global memoryCount
    print input
    hexList = re.findall (r'\\x[0-9A-Fa-f]{2}', input)
    hexList.extend(re.findall (r'\\\"', input))
    hexList.extend(re.findall (r'\\\\', input))

    for hex in hexList:
        input = input.replace(hex, '')

    print hexList
    print input
    print str(len(input)) +  "+" + str(len(hexList))
    memoryCount = memoryCount + len(input) + len(hexList)

def cleanCount(input):
    clean = input[1:-1] #-2 to remove \n at the end of the line.
    replace_hex(clean)

with open('data.txt') as f:
    content = f.read().replace(' ','').splitlines()
    codeCount = reduce(lambda x,y: x+y, map(lambda x: len(x), content))
    map(lambda x: (cleanCount(x)), content)
    print str(codeCount-memoryCount)

