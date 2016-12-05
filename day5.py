#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import md5
import hashlib

secretKey = 'ugkcyxxp'
possibleValue = 0
evaluatedValue = None

# Part 1
i = 0
c = 0
r = []
while(1):
    evaluatedValue = (secretKey + str(i))
    possibleValue = hashlib.md5(secretKey + str(i)).hexdigest()
    if possibleValue.startswith("00000"):
        r.append(possibleValue[5])

        c = c+1
        if c == 8:
            break
    i = i + 1

print "".join(r)


# Part 2
i = 0
c = 0
r = []
for i in range(8):
    r.append(-1)

while(1):
    evaluatedValue = (secretKey + str(i))
    possibleValue = hashlib.md5(secretKey + str(i)).hexdigest()
    if possibleValue.startswith("00000"):
        index = possibleValue[5]
        value = possibleValue[6]
        if index.isdigit() and int(index) < 8 and r[int(index)] == -1:
            r[int(index)] = value
            c = c+1

            if c == 8:
                break

    i = i + 1

print "".join(r)
