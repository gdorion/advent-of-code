#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

puzzleInput = 'L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2'

# puzzleInput = 'R2, L3'
# puzzleInput = 'R5, L5, R5, R3'
# puzzleInput = 'R2, R2, R2'
# puzzleInput = 'R8, R4, R4, R8'
puzzleInput = puzzleInput.replace(' ', '')
directions = puzzleInput.split(',')

result = 0
x = 0
y = 0
found = False

coordsx = [0]
coordsy = [0]
current = 'N'

for direction in directions:
    d = direction[0]
    s = int(direction[1:])

    for i in range(s):
        if current == 'N' and d == 'L':
            x -= 1
            if i == s - 1:
                current = 'W'

        elif current == 'N' and d == 'R':
            x += 1
            if i == s - 1:
                current = 'E'
        elif current == 'E' and d == 'L':
            y += 1
            if i == s - 1:
                current = 'N'
        elif current == 'E' and d == 'R':
            y -= 1
            if i == s - 1:
                current = 'S'
        elif current == 'S' and d == 'L':
            x += 1
            if i == s - 1:
                current = 'E'
        elif current == 'S' and d == 'R':
            x -= 1
            if i == s - 1:
                current = 'W'
        elif current == 'W' and d == 'L':
            y -= 1
            if i == s - 1:
                current = 'S'
        elif current == 'W' and d == 'R':
            y += 1
            if i == s - 1:
                current = 'N'

        for i in range(len(coordsx)):
            if x == coordsx[i] and y == coordsy[i] and found == False:
                print '#2 : ' + str(x) + ', ' + str(y)
                print '#2 distance : ' + str(abs(x) + abs (y))
                found = True
                break

        coordsx.append(x)
        coordsy.append(y)

print '#1 : ' + str(abs(x) + abs (y))
