#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

i = 0

with open('data.txt') as f:
    for c in f.read():
	if c == '(':
            i = i+1
        elif c == ')' :
            i = i-1

print 'Results is ' + str(i)

