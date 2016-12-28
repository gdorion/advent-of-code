#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#
import copy

def initDict():
    dict = {}
    for i in range(300):
        dict[i] = [];
    return dict

def process(instructs):
    bots = initDict()
    outputs = initDict()

    for instruct in copy.deepcopy(instructs):
        if 'goes to' in instruct:
            val = int(instruct.split(' ')[1])
            bot_id = int(instruct.split(' ')[5])

            if bots.has_key(bot_id):
                bots[bot_id].append(val)
            else:
                bots[bot_id] = [val]
            
            instructs.remove(instruct)

    while len(instructs) > 0:
        for instruct in copy.deepcopy(instructs):
            destDictLow = outputs if 'low to output' in instruct else bots
            destDictHigh = outputs if 'high to output' in instruct else bots
            source = int(instruct.split(' ')[1])
            destLow = int(instruct.split(' ')[6])
            destHigh = int(instruct.split(' ')[11])

            if bots[source]:
                low = min(bots[source])
                high = max(bots[source])

                if len(bots[source]) >= 2:
                    destDictLow[destLow].append(low)
                    bots[source].remove(low)

                    destDictHigh[destHigh].append(high)
                    bots[source].remove(high)

                    instructs.remove(instruct)

                    if low == 17 and high == 61:
                        print source

    print outputs
    print "Part 2: " + str(int(outputs[0][0] * outputs[1][0] * outputs[2][0]))

inp = []
with open('day10.txt') as f:
# with open('day10test.txt') as f:
    inp = f.read().splitlines()

process(inp)

