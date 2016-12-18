#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import json

escapeCount = 0

def escape(input):
    global escapeCount
    escapeCount = escapeCount + len(json.dumps(input))

with open('data.txt') as f:
    content = f.read().replace(' ','').splitlines()
    codeCount = reduce(lambda x,y: x+y, map(lambda x: len(x), content))
    map(lambda x: (escape(x)), content)
    print str(escapeCount-codeCount)


