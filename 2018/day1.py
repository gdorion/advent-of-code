#!/usr/bin/env python
sum = 0
with open('day1.txt') as f:
    rows = []
    for line in f:
        rows.append(line.rstrip())
    
    for r in rows:
      if r[0] == '-':
        r = r[1:]
        val = int(r)
        sum -= val
      elif r[0] == '+':  
        r = r[1:]
        val = int(r)
        sum += val

      print sum
