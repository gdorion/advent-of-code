#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import regex as re

niceStringsCount = 0

azRE = re.compile("[A-Za-z]+")
doubleLetterRE = re.compile(r"([a-z][a-z])")
notContainingList = re.compile("[A-Za-z]+")
repeatedChars = re.compile("[A-Za-z]+")

with open('data.txt') as f:
    for line in f:

        match = False
        matchString = line + " -> "

        if azRE.match(line) :
            matchString = matchString + 'a-z'

            results = []
            for idx, c in enumerate(line):
                if idx + 1 < len(line) and line[idx+1] != '\n':
                    results.append(c + line[idx+1])

            for string in results:
                location = re.findall(string, line, overlapped=False)
                if len(location) > 1:
                    matchString = matchString + str(location)
                    match = True
                    break

            if match:
                match = False
                for idx, c in enumerate(line):
                    repeatingCharLoc = idx
                    if idx + 1 < len(line):
                        seperatorLoc = idx + 1
                        if idx + 2 < len(line):
                            if line[repeatingCharLoc] == line[idx + 2]:
                                match = True
                                matchString = matchString + " %s%s%s " %  (line[repeatingCharLoc], line[seperatorLoc], line[idx + 2])
                                print matchString
                                break



        if match:
            #print 'Match found: ', match.group()
            niceStringsCount = niceStringsCount + 1

print "Nice strings count : " + str(niceStringsCount)

