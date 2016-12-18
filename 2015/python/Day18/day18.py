#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import copy

col = 100
row = 100
grid = []
step = 100

initial =   '.#.#.# '\
            '...##. '\
            '#....# '\
            '..#... '\
            '#.#..# '\
            '####..'
charGrid = initial.split(' ')

initial = open('data.txt').read().splitlines()
charGrid = initial

def onMap(grid, x, y):
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

def findNeighbours(grid, x, y):
    neighbours = []

    # Top-left
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            if xx == 0 and yy == 0:
                continue

            if onMap(grid, x + xx, y + yy):
                neighbours.append(grid[x + xx][y + yy])

    return neighbours

def animate(grid):
    newGrid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbours = findNeighbours(grid,i,j)

            # on
            state = grid[i][j]
            nOn = 0
            for n in neighbours:
                if n == 1:
                    nOn = nOn + 1

            if state == 1:
                if nOn == 2 or nOn == 3:
                    state = 1
                else:
                    state = 0
            else:
                if nOn == 3:
                    state = 1
                else:
                    state = 0

            newGrid[i][j] = state
    return newGrid

def lightCounts(grid):
    onCount = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                onCount = onCount + 1
    return onCount

def printGrid(grid):
    for row in grid:
        print str(row) + '\n'
    print '--------------------------------'

# Init grid
for i in range(row):
    row = []
    for j in range(col):
        row.append(0)
    grid.append(row)

# Set initial value in grid
for i, stringLine in enumerate(charGrid):
    for j, c in enumerate(stringLine):
        grid[i][j] = 0 if c == '.' else 1

for i in range(step):
    grid = animate(grid)
    print i

print lightCounts(grid)
