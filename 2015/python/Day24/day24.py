#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import itertools
import numpy

numbers = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def balance(target):
    quantum = 9999999999999999
    combinations = itertools.combinations(numbers, 5) # nothing with 5 elements

    for c in combinations:
        if sum(c) == target:
            quantum = min(quantum, numpy.prod(c))

    print quantum

# Part1
balance(sum(numbers) / 3)
balance(sum(numbers) / 4)
