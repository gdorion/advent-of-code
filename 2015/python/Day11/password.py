#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import re

def hasPairs(input):
    pairs = []
    for idx, c in enumerate(input):
        if idx + 1 < len(input):
            pairs.append(c + input[idx+1])

    num = 0
    for idx, pair in enumerate(pairs):
        if pair[0] == pair[1]:
            if idx > 0 and pair == pairs[idx-1]:
                continue
            num = num + 1
    has = num == 2
    return has

def inExclusion(char):
    if chr(char) in ['i', 'o', 'l']:
        return 1
    return 0

def hasStraight(input):
    for i in range(len(input)):
        if i > 0:
            if i + 1 < len(input):
                before = ord(input[i-1])
                after  = ord(input[i+1])
                current = ord(input[i])

                if (current - before == 1) and (after - current == 1):
                    return True
    return False

def hasExclusions(input):
    for i in range(len(input)):
        char = ord(input[i])
        if inExclusion(char) == 1:
            return True

    return False


def isValid(input):
    return hasPairs(input) and hasStraight(input) and hasExclusions(input) == False

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

#part 1
string = 'hxbxwxba'
while isValid(string) == False:
    increment = 1
    if inExclusion(ord(string[len(string)-1])):
        increment = 2
    string = str_base(int(string, 36) + increment , 36).replace('0','a')

print string
raw_input("Tap for next iteration")
string = str_base(int(string, 36) + increment , 36).replace('0','a')

#part 2
while isValid(string) == False:
    increment = 1
    if inExclusion(ord(string[len(string)-1])):
        increment = 2
    string = str_base(int(string, 36) + increment , 36).replace('0','a')

print string
