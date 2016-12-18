#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
import operator

def incrementKey(key, dict):
    if key in dict.keys():
        dict[key] = dict[key] + 1
    else:
        dict[key] = 0
    return dict


maxresults = []
minresults = []

for i in range(8):
    colResults = {}
    with open('day6.txt') as f:
        for line in f:
            colResults = incrementKey(line[i], colResults)

    maxresults.append(max(colResults, key=colResults.get))
    minresults.append(min(colResults, key=colResults.get))

print "".join(maxresults)
print "".join(minresults)
