#!/usr/bin/env python
score = 0

with open('day2.txt') as f:
    rows = []
    for line in f:
        rows.append(map(int, line.rstrip().split()))

    checksum = 0
    b_result = 0
    for row in rows:
        mmax = max(row)
        mmin = min(row)
        checksum = checksum + (mmax-mmin)

        for i in row:
            for j in row:
                if i % j == 0 and i != j:
                    b_result += (i / j)

    print checksum
    print b_result