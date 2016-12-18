#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

paperRequired = 0 # In Square feet

with open('data.txt') as f:
    for line in f:
        parameters = line.split('x')
        l = int(parameters[0])
        w = int(parameters[1])
        h = int(parameters[2])

        sl = 2 * l * w
        sw = 2 * w * h
        sh = 2 * h * l

        surfaceValues = [l * w, w * h, h * l]

        lineTotal = sl + sw + sh
        print 'Line total is          ' + str(lineTotal)

        lineTotal = lineTotal + min(surfaceValues)
        print 'Surface Values : ' + str(surfaceValues)
        print 'Min(surfaceValues) is  ' + str( min(surfaceValues))
        print 'Paper Required for line : ' + str(lineTotal)

        paperRequired = paperRequired + lineTotal



print 'Total paper needed is ' + str(paperRequired)

