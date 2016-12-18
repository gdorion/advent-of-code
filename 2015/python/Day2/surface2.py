#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

paperRequired = 0 # In Square feet

with open('./data.txt') as f:
    for line in f:
        parameters = line.split('x')
        l = int(parameters[0])
        w = int(parameters[1])
        h = int(parameters[2])

        params = [l,w,h]

        minParam = min(params)
        params.remove(minParam)
        secondMinParam = min(params)

        total = (2 * minParam) + (2 * secondMinParam)

        cubicVolume = l * w * h

        paperRequired = paperRequired + total + cubicVolume

        print '2 * ' + str(minParam) + ' + 2 * ' + str(secondMinParam)
        print 'Cubic Vol : ' + str(cubicVolume)

    print 'Total :' + str(paperRequired)

