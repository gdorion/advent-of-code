#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

raw = open('day12.txt').read().splitlines()
registers = {'a': 0, 'b': 0, 'c' : 1, 'd' : 0}

instructions = []
for l in raw:
    components = l.split(' ')
    ins = components[0]
    rid = components[1]

    offset = 0
    if len(components) > 2:
        offset = components[2]

    instructions.append([ins, rid, offset])

def getValue(value):
    try:
        return int(value)
    except ValueError:
        return registers[value]

def evaluate(exp):
    if '-' in exp:
        return int(exp.split('-')[1]) * -1
    elif exp.isdigit():
        return int(exp)

    return None

def compute(instructions, startValue):
    registers['c'] = startValue
    i = 0
    while i < len(instructions):
        ins = instructions[i]
        # print '%s -> i: %s, Registers:  %s]' % (ins, str(i), str(registers)) + 'before'

        if ins[0] == 'cpy':
            val = getValue(ins[1])
            registers[ins[2]] = val

        elif ins[0] == 'inc':
            registers[ins[1]] += 1

        elif ins[0] == 'dec':
            registers[ins[1]] -= 1

        elif ins[0] == 'jnz':
            if getValue(ins[1]) != 0 :
                i += evaluate(ins[2])
                continue

        i += 1

        # print '%s -> i: %s, Registers:  %s]' % (ins, str(i), str(registers)) + 'after\n'

compute(instructions, 0)
print registers['a']
compute(instructions, 1)
print registers['a']




