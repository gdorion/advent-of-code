#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

import re

# Parse rules and string
content = open('data.txt').read()
rules = re.findall('([\w]+) => ([\w]+)', content)
content = re.findall('([\w]+)', content)
string = content[len(content)-1]

results = set()

for r in rules:
    for i in range(len(string)):
        if r[0] == string[i:i + len(r[0])]:
            results.add(string[:i] + r[1] + string[i + len(r[0]):])

print len(results)

# Part 2

count = 0
while string != 'e':
    for r in rules:
        if r[1] in string:
            string = string.replace(r[1], r[0], 1) # Only replace 1 occurence per try
            count = count + 1

print count

