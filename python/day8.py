#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
board_width = 50
board_height = 6
board = [][]
for x in range(len(board_width)):
    for y in range(len(board_height)):
        board[x][y] = 0

# with open('day7TestInput2.txt') as f:
with open('day8.txt') as f:
    for line in f:
        if 'rect' in line:
            a = int(line.split(' ')[1].split('x')[0])
            b = int(line.split('x')[1])

            for x in range(len(a)):
                for y in range(len(b)):
                    board[x][y] = 1

        elif 'rotate row' in line:
            a = line.split(' ')[2].split('=')[1] #col
            b = line.split(' ')[4] #value

            for y in range(len(b))):
                # todo !
                # board[a][y] = 1

        elif 'rotate column' in line:
            a = line.split(' ')[2].split('=')[1]
            b = line.split(' ')[4]
