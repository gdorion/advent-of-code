#!/usr/bin/env python
N, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0) # directions
turn_left = {N: W, E: N, S: E, W: S} # old -> new direction
inp = 1024


x = 0
y = 0
direction = S
for i in range(inp):
    x += turn_left[direction][0]
    y += turn_left[direction][1]
    direction = turn_left[direction]


print x
print y