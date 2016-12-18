#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import itertools

def permutations(people):
    results = []
    for i in range(len(people)):
        row = []
        for j in range(len(people)):
            row.append(people[j])
        results.append(row)
    return results

def leftOf(person, people):
    for i, p in enumerate(people):
        if p == person:
            if i == 0:
                return people[len(people) - 1];
            else:
                return people[i-1]
    return None

def rightOf(person, people):
    for i, p in enumerate(people):
        if p == person:
            if i == len(people)-1:
                return people[0];
            else:
                return people[i+1]
    return None

seats = []
people = set()
preferences = []

with open('data.txt') as f:
    for line in f:
        l = line.rstrip('\n')
        components = l.split('.')[0].split(' ')

        people.add(components[0])
        people.add(components[10])

        unit = int(components[3])

        if components[2] == 'lose':
            unit = unit * -1

        preferences.append([components[0], components[10], unit])

possibleSeats = itertools.permutations(list(people))

happinessList = []
for seating in possibleSeats:
    seatingResults = []

    for i, person in enumerate(seating):
        seatingResults.append(0)

    for pref in preferences:
        for i, person in enumerate(seating):

            if person == pref[0]:
                if pref[1] == leftOf(person, seating) or pref[1] == rightOf(person, seating):
                    seatingResults[i] = seatingResults[i] + pref[2]

    happinessList.append(seatingResults)

totalList = []
for happinessResults in happinessList:
    total = 0
    for result in happinessResults:
        total = total + result
    totalList.append(total)

maxValue = 0
for total in totalList:
    if total > maxValue:
        maxValue = total

print people
print maxValue








