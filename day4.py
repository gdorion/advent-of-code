import operator
from collections import defaultdict

def validate(string, checksum):
    s_registry = {}

    for i, c in enumerate(string):
        if c in s_registry.keys():
            s_registry[c] = s_registry[c] + 1
        else:
            s_registry[c] = 1

    sorted_s = [v for v in sorted(s_registry.iteritems(), key=lambda(k, v): (-v, k))]
    
    for i in range(len(checksum)):
        checksumLetter = checksum[i]
        roomLetter = sorted_s[i][0]
        if checksumLetter != roomLetter:
            return False
    return True

sum = 0
with open('day4.txt') as f:
    rows = []
    for line in f:
        rows.append(line.rstrip())

    for row in rows:
        lettersSections = row.split('[')[0].split('-')
        checksum = row.split('[')[1].split(']')[0]
        sectorId = lettersSections[len(lettersSections)-1];
        lettersSections.pop(len(lettersSections)-1)
        rawString = "".join(lettersSections)

        if validate(rawString, checksum):
            sum = sum + int(sectorId)

print sum
