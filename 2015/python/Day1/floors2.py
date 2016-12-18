#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

floorNumber  = 0
charPosition = 1

with open('data.txt') as f:
    for c in f.read():
        if c == '(':
            floorNumber = floorNumber+1
        elif c == ')' :
            floorNumber = floorNumber-1

        if floorNumber == -1:
            break

        charPosition = charPosition + 1

print 'Results is ' + str(floorNumber) + ' at position ' + str(charPosition)
