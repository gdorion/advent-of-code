#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
# For answer in part 2 : look in screen about
    #  upojflbcez
from copy import deepcopy

numberRow = 6
numberCol = 50

matrix = []
for i in range(0,numberRow):
    row = []
    for j in range(0,numberCol):
        row.append(0)
    matrix.append(row)

def printMatrix(matrix):
    for row in matrix:
        print str(row) + "\n"

def getOffset(initial, offset, total):
    result = initial
    for i in range(offset):
        result = result - 1
        if result < 0:
            result = total - 1
    return result

with open('day8.txt') as f:
# with open('day8Test.txt') as f:
    for line in f:
        copy = []
        if 'rect' in line:
            a = int(line.split(' ')[1].split('x')[0]) #width
            b = int(line.split(' ')[1].split('x')[1]) #height

            for x in range(b):
                for y in range(a):
                    matrix[x][y] = 1

            # printMatrix(matrix)

        elif 'rotate column' in line:
            col = int(line.split(' ')[2].split('=')[1]) #col
            val = int(line.split(' ')[4]) #val

            copy = deepcopy(matrix)
            for row in range(numberRow):
                offset = getOffset(row, val, numberRow)
                matrix[row][col] = copy[offset][col]

            # printMatrix(matrix)

        elif 'rotate row' in line:
            row = int(line.split(' ')[2].split('=')[1]) #row
            val = int(line.split(' ')[4]) #val

            copy = deepcopy(matrix)
            for col in range(numberCol):
                offset = getOffset(col, val, numberCol)
                matrix[row][col] = copy[row][offset]

            # printMatrix(matrix)
printMatrix(matrix)
lightsCount = 0
for i in range(0,numberRow) :
    for j in range(0,numberCol):
        if matrix[i][j] == 1:
            lightsCount = lightsCount + 1
print lightsCount
