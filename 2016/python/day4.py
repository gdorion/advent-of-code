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

def decrypt(c):
    if c == 'z':
        c = 'a'
    elif c == 'Z':
        c = 'A'
    elif c != ' ':
        c = chr(ord(c) + 1)
    return c

def rotate(string, count):
    result = ""
    for c in string:
        newC = c
        for i in range(count):
            newC = decrypt(newC)
        result += newC
    return result

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

        # part1
        if validate(rawString, checksum):
            sum = sum + int(sectorId)

        lettersSections = row.split('[')[0].split('-')
        lettersSections.pop(len(lettersSections)-1)
        roomName = " ".join(lettersSections)
        decrypted = rotate(roomName, int(sectorId))
        if "north" in decrypted:
            print decrypted
            print sectorId

print sum
