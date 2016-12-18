#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import md5
import hashlib

secretKey = 'yzbqklnj'
possibleValue = 0
evaluatedValue = None

i = 0
while(1):
    evaluatedValue = (secretKey + str(i))
    possibleValue = hashlib.md5(secretKey + str(i)).hexdigest()
    if possibleValue.startswith("00000"):
        break;
    i = i + 1

print evaluatedValue


