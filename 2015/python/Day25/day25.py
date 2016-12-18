#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

r = 2978
c = 3083
p = (r + c) * (r + c - 1) // 2 - r + 1 # Rocket science frozen meal. Get the linear index of the cell's position
result = 20151125

for i in range(p - 1):
    result = (result * 252533) % 33554393

print result
