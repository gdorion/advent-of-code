#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

input = "1321131112"

def generate(input):
    result = ""
    count = 1
    i = 0

    while(i < len(input)):
        c = input[i]

        if i+1 < len(input):
            if c == input[i+1]:
                count = count+1
            else:
                result = result + ("%s%s" % ( str(count), c))
                count = 1
        else:
            result = result + ("%s%s" % ( str(count), c))
            count = 1
        i=i+1

    return result

# Part 1
result = input
for i in range(40):
    result = generate(result)
print "Part 1:" + str(len(result))

# Part 2
result = input
for i in range(50):
    result = generate(result)

print "Part 2:" + str(len(result))
