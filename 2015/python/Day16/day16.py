#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

from operator import attrgetter

class Sue(object):
    def __init__(self, number, attributes):
        self.number = number
        self.attributes = attributes
        self.cluesMatchCount = 0

aunts = []
clues = {"children": 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

with open('data.txt') as f:
    for line in f:
        l = line.rstrip('\n')
        l = l.replace(':','')
        l = l.replace(',','')

        params = l.split('.')[0].split(' ')
        print params
        aunts.append(Sue(params[1], { params[2] : int(params[3]), params[4] : int(params[5]), params[6] : int(params[7])}))

suspects = []
for sue in aunts:
    cluesMatchClues = 0

    for keySueAtt, value in sue.attributes.iteritems():
        if keySueAtt == 'children':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'cats':
            if sue.attributes[keySueAtt] > clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'samoyeds':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'pomeranians':
            if sue.attributes[keySueAtt] < clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'akitas':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'vizslas':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'goldfish':
            if sue.attributes[keySueAtt] < clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'trees':
            if sue.attributes[keySueAtt] > clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'cars':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

        elif keySueAtt == 'perfumes':
            if sue.attributes[keySueAtt] == clues[keySueAtt]:
                cluesMatchClues = cluesMatchClues + 1

    sue.cluesMatchCount = cluesMatchClues

guess = max(aunts, key=attrgetter('cluesMatchCount'))
print guess.number
