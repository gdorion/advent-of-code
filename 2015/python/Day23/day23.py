#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

raw = open('data.txt').read().splitlines()

instructions = []
for l in raw:
    components = l.split(' ')
    ins = components[0]
    rid = components[1].replace(',','')
    offset = '+0'

    if ins == 'jmp':
        offset = components[1]
    elif ins in ['jio', 'jie']:
        offset = components[2]

    instructions.append([ins, rid, offset])

registers = {'a': 1, 'b':0}

def evaluate(exp):
    if '+' in exp:
        return int(exp.split('+')[1])
    if '-' in exp:
        print int(exp.split('-')[1]) * -1
        return int(exp.split('-')[1]) * -1

def process(ins, rid, offset):
    global registers, instructions

    if ins == 'hlf':
        registers[rid] /= 2
    elif ins == 'tpl':
        registers[rid] *= 3
    elif ins == 'inc':
        registers[rid] += 1
    elif ins == 'jmp':
        return evaluate(offset)
    elif ins == 'jie':
        if registers[rid] % 2 == 0:
            return evaluate(offset)
    elif ins == 'jio':
        if registers[rid] == 1:
            return evaluate(offset)

    return 0

i = 0
while i < len(instructions):
    ins = instructions[i]
    print '%s -> i: %s, Registers:  %s]' % (ins, str(i), str(registers)) + 'before'
    offset = process(ins[0], ins[1], ins[2])

    if offset == 0:
        offset = 1

    i += offset

    print '%s -> i: %s, Registers:  %s]' % (ins, str(i), str(registers)) + 'after'

print registers['b']


