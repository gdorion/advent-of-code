#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

numberRow = 999
numberCol = 999

matrix = []
for i in range(0,numberRow+1):
    row = []
    for j in range(0,numberCol + 1):
        row.append(0)
    matrix.append(row)

def printMatrix():
    for row in matrix:
        print str(row) + "\n"

def findX(coordinate):
    return int(coordinate.split(',')[0])

def findY(coordinate):
    return int(coordinate.split(',')[1])

def turnon(start, through, activate):
    startX = findX(start)
    startY = findY(start)
    endX = findX(through)
    endY = findY(through)

    for i in range(startX,endX+1):
        for j in range(startY,endY+1):
            if activate == 1:
                matrix[i][j] = matrix[i][j] + 1
            else:
                matrix[i][j] = max(matrix[i][j] - 1, 0) # do not go below 0.

def toggle(start, through):
    startX = findX(start)
    startY = findY(start)
    endX = findX(through)
    endY = findY(through)

    for i in range(startX,endX+1):
        for j in range(startY,endY+1):
             matrix[i][j] =  matrix[i][j] + 2

with open('data.txt') as f:
    for line in f:
        components = line.rstrip('\n').split(' ')

        if components[0] == 'turn':
            if components[1] == 'on':
                turnon(components[2], components[4], 1)
            elif components[1] == 'off':
                turnon(components[2], components[4], 0)

        elif components[0] == 'toggle':
            toggle(components[1], components[3])

totalBrightness = 0
for i in range(0,numberRow+1) :
    for j in range(0,numberCol+1):
        totalBrightness = totalBrightness + matrix[i][j]

print totalBrightness
