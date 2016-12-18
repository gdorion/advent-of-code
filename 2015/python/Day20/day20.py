#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

from collections import defaultdict

inp = 29000000

# (VERY LONG)
def find(inp, top):
    houses = defaultdict(int)

    for i in xrange(1, inp):
        for j in xrange(i, top, i):
            houses[j]+= (i * 10)

        if houses[i] >= inp:
            print i
            return

        print i
        print houses[i]

def find2(inp, top):
    houses = defaultdict(int)

    for i in xrange(1, inp):
        for j in xrange(i, min(i*50+1, top), i):
            houses[j]+= (i * 11)

        if houses[i] >= inp:
            print i
            return

#find(inp, 1000000)
find2(inp, 1000000)
