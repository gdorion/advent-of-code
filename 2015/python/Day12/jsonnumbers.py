#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import json

content = open('data.txt', 'r').read()
data  = json.loads(content)

total = 0

def deeper(data):
    global total
    if isinstance(data, dict):
        for k, v in data.iteritems():
            deeper(v)
    elif isinstance(data, list):
        for k in list(data):
            deeper(k)
    elif isinstance(data, int):
        total = total + int(data)

deeper(data)

print total
