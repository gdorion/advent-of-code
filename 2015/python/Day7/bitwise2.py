#!/bin/env python
#
#     Adventofcode.com
#
# Author : Guillaume Dorion
# Email  : gdorion@gmail.com
#

nodes = []
wires = []

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def updatedWire(wire):
    global wires
    for w in wires:
        if w.name == wire.name:
            return w
    return wire

class Wire(object):
    def __init__(self, value):
        self.name = None
        self.value = None

        if value != None and is_number(value):
            self.value = int(value)
        else:
            self.name = value

    def __str__(self):
        return "%s=%s" % (self.name, self.value)
    def __repr__(self):
        return str(self)

class Node(object):
    def __init__(self, firstInput, secondInput, output, operation):
        self.firstInput = firstInput
        self.secondInput = secondInput
        self.output = output
        self.operation = operation

    def __str__(self):
        if self.secondInput == None:
            return "%s %s -> %s" % (str(self.firstInput), self.operation, str(self.output))
        return "%s %s %s -> %s" % (str(self.firstInput), self.operation, str(self.secondInput), str(self.output))

    def __repr__(self):
        return str(self)

    def compute(self):
        self.firstInput = updatedWire(self.firstInput)
        self.output = updatedWire(self.output)

        if self.firstInput.name == 'b':
            self.firstInput.value = 16076 # It's the A value of the part 1

        if self.secondInput :
            self.secondInput = updatedWire(self.secondInput)
            if self.secondInput.name == 'b':
                self.secondInput.value = 16076 # It's the A value of the part 1

        # Direct operation (no transformation needed)
        if self.operation == "":
            if self.firstInput.value != None:
                self.output.value = self.firstInput.value
                return True

        elif self.operation == 'AND':
            if self.firstInput.value != None and self.secondInput.value != None:
                self.output.value = self.firstInput.value & self.secondInput.value
                return True

        elif self.operation == 'OR':
            if self.firstInput.value != None and self.secondInput.value != None:
                self.output.value = self.firstInput.value | self.secondInput.value
                return True

        elif self.operation == 'NOT':
            if self.firstInput.value != None:
                self.output.value = ~self.firstInput.value
                return True

        elif 'RSHIFT' in self.operation:
            components = self.operation.split(' ')

            if self.firstInput.value != None :
                self.output.value = self.firstInput.value >> int(components[1])
                return True

        elif 'LSHIFT' in self.operation:
            components = self.operation.split(' ')
            if self.firstInput.value != None :
                self.output.value = self.firstInput.value << int(components[1])
                return True

        return False

def appendOrUpdateWire(wire):
    global wires
    found = False
    for w in wires:
        if w.name == wire.name :
            if wire.value >= 0:
                w.value = wire.value
            found = True

    if found == False:
        wires.append(wire)

# bo OR bu -> bv
# lf AND lq -> ls
def andOrOperatorNode(line):
    global nodes
    components = line.split(' ')

    wireInput = Wire(components[0])
    wireInput2 = Wire(components[2])
    wireOutput = Wire(components[4])

    appendOrUpdateWire(wireInput)
    appendOrUpdateWire(wireInput2)
    appendOrUpdateWire(wireOutput)

    node = Node(wireInput, wireInput2, wireOutput, components[1])
    nodes.append(node)

# jm LSHIFT 1 -> kg
# jm RSHIFT 1 -> kg
def shiftOperatorNode(line):
    global nodes
    components = line.split(' ')

    wireInput = Wire(components[0])
    wireOutput = Wire(components[4])
    appendOrUpdateWire(wireInput)
    appendOrUpdateWire(wireOutput)

    node = Node(wireInput, None, wireOutput, "%s %s" % (components[1], components[2]))
    nodes.append(node)

# NOT fx -> fy
def notOperatorNode(line):
    global nodes
    components = line.split(' ')

    wireInput = Wire(components[1])
    wireOutput = Wire(components[3])
    appendOrUpdateWire(wireInput)
    appendOrUpdateWire(wireOutput)

    node = Node(wireInput, None, wireOutput, "NOT")
    nodes.append(node)

# 19138 -> b
# lx -> a
def completeOperationNode(line):
    global nodes
    components = line.split(' ')
    if is_number(components[0]):
        wireOutput = Wire(components[0])
        wireOutput.name = components[2] # In this case the value at init time is a constant. So we reset it inside the object.
        appendOrUpdateWire(wireOutput)
    else:
        wireInput = Wire(components[0])
        wireOutput = Wire(components[2])
        appendOrUpdateWire(wireInput)
        appendOrUpdateWire(wireOutput)

        node = Node(wireInput, None, wireOutput, "")
        nodes.append(node)

# Backtracking algo
def processNodes(nodes):
    i = len(nodes) - 1
    while i >= 0:
        node = nodes[i]
        if node.compute():
            appendOrUpdateWire(node.output)
            nodes.remove(node)
        i = i - 1

def printValues():
    global wires
    for w in wires:
        if w.value != None :
            print w

def main():
    global wires
    global nodes
    nodes = []
    wires = []

    with open('data.txt') as f:
        for line in f:
            l = line.rstrip('\n')
            if 'AND' in l or 'OR' in l:
                andOrOperatorNode(l)
            elif 'LSHIFT' in l or 'RSHIFT' in l:
                shiftOperatorNode(l)
            elif 'NOT' in l:
                notOperatorNode(l)
            else:
                completeOperationNode(l)

    print wires

    while len(nodes) > 0:
        processNodes(nodes)

    printValues()

if __name__ == "__main__":
    main()


