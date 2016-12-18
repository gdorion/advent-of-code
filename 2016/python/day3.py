#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com

possibleTriangles = []

with open('day3.txt') as f:
    rows = []
    for line in f:
        rows.append(line.rstrip().split('  '))

clean_values = []
for row in rows:
    clean_row = []
    for val in row:
        if val != '':
            clean_row.append(int(val))
    if len(clean_row) > 0:
        clean_values.append(clean_row)

def isValid(triangle):
    return (t[0] + t[1] > t[2]) and (t[1] + t[2] > t[0]) and (t[2] + t[0] > t[1])

# part 1
for t in clean_values:
    if isValid(t):
        possibleTriangles.append(t)

print len(possibleTriangles)

# Part 2
row = 0
possibleTriangles = []
for i in xrange(0, len(clean_values), 3):
    for j in range(3):
        t = [clean_values[i][j], clean_values[i+1][j], clean_values[i+2][j]]
        if isValid(t):
            possibleTriangles.append(t)
print len(possibleTriangles)
