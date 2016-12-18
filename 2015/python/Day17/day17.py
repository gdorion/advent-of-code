#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import itertools

def powerset(l):
    return itertools.chain.from_iterable((itertools.combinations(l, i) for i in range(len(l)+1)))

def filterInput(containers, goal):
    return filter(lambda v: sum(v) == goal and len(v) == 4, powerset(containers)) #Part 2
#Part 1    return filter(lambda v: sum(v) == goal, powerset(containers))

# Test
# Part 1
containers = sorted([20, 15, 10, 5, 5], reverse=True)
filtered = filterInput(containers, 25)
filtered.append((10, 15))
#print list(clearDuplicate(filtered))
#print len(list(clearDuplicate(filtered)))


# Part 2
#containers = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
containers = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]


print str(len(filterInput(containers, 150)))
#print filterInput(containers, 150)
