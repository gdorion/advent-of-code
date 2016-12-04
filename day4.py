import operator
from collections import defaultdict

def validate(string, checksum):
    s_registry = {}

    for i, c in enumerate(string):
        if c in s_registry.keys():
            s_registry[c] = s_registry[c] + 1
        else:
            s_registry[c] = 0

    sorted_s = sorted(s_registry.items(), key=operator.itemgetter(1), reverse=True)

    # print s_registry
    print sorted_s
    print checksum

    for i in range(len(checksum)):
        if sorted_s[i][0] != checksum[i]:
            for j in xrange(0, len(checksum)):
                if sorted_s[i] == sorted_s[j]:
                    foundEquivalent = True
                    break

            if foundEquivalent:
                return True

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
