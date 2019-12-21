# PART 1
f = open('inputs/2.txt')
# f = open('inputs/2.test.txt')
content = f.read().splitlines()[0].split(',')
initialContent = list(content)
content[1] = 12
content[2] = 2

instuct_len = 4


def processOpCode(content):
    index = 0
    while index + 3 < len(content):
        opcode = int(content[index])
        if opcode == 1:
            pos1 = int(content[index + 1])
            pos2 = int(content[index + 2])
            pos3 = int(content[index + 3])
            if (pos3 < len(content)):
                content[pos3] = int(content[pos1]) + int(content[pos2])

        elif opcode == 2:
            pos1 = int(content[index + 1])
            pos2 = int(content[index + 2])
            pos3 = int(content[index + 3])
            if (pos3 < len(content)):
                content[pos3] = int(content[pos1]) * int(content[pos2])

        elif opcode == 99:
            return content[0]

        index += instuct_len


processOpCode(content)
print content[0]


# PART 2
val1 = 0
val2 = 0

for i in range(0, 99):
    for j in range(0, 99):
        newContent = list(initialContent)
        newContent[1] = i
        newContent[2] = j
        val = processOpCode(newContent)
        if val == 19690720:
            print 100 * i + j
            print val
            exit()
