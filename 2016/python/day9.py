#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
def decompressRecursive(content, part):
    if '(' not in content:
        return len(content)
    else:
        print content

    pos = 0

    while '(' in content:
        ms = content.find('(')
        pos += ms
        content = content[ms:]

        me = content.find(')')
        marker = content[1:me].split('x')
        content = content[me+1:]

        original = content[:int(marker[0])]
        extended = int(marker[1])
        if part == 2:
            pos += decompressRecursive(original, part) * extended
        else:
            pos += len(original * extended)
        content = content[int(marker[0]):]

    pos += len(content)
    return pos

s = open('day9.txt').read().strip()
print decompressRecursive(s, 1)
print decompressRecursive(s, 2)

