#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import re

niceStringsCount = 0

azRE = re.compile("[A-Za-z]+")
vowelRE = re.compile("[aeiou]")
doubleLetterRE = re.compile(r"[a-z]*([a-z])\1([a-z])*")
notContainingList = ['ab', 'cd', 'pq', 'xy']

with open('data.txt') as f:
    for line in f:

        match = False
        matchString = line + " -> "

        if azRE.match(line) :
            matchString = matchString + 'a-zRE'

            if len(vowelRE.findall(line)) >= 3:
                print str(vowelRE.findall(line))
                matchString = matchString + ', vowelRE'

                if doubleLetterRE.match(line) :
                    matchString = matchString + ', doubleLetterRE'

                    for string in notContainingList:
                        location = re.search(string, line)
                        if location > 0:
                            match = False
                            break

                        match = True
                        matchString = matchString + ', not have ' + string

        print matchString
        if match:
            #print 'Match found: ', match.group()
            niceStringsCount = niceStringsCount + 1

print "Nice strings count : " + str(niceStringsCount)
