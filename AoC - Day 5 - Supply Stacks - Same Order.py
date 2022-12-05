from collections import deque

cargo = []
isCargoInputDone = False

commands = []

def stack_move_multiple(stackSrc, stackDst, num):
    tempStack = deque()
    for i in range(num):
        x = stackSrc.pop()
        tempStack.append(x)

    for j in range(num):
        y = tempStack.pop()
        stackDst.append(y)
    return stackSrc, stackDst


with open('input5.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        if not isCargoInputDone:
            if i == "\n":
                isCargoInputDone = True
                continue
            cargo.append(i.rstrip("\n"))
        else:
            command = i.split()
            commandNumbers = [int(command[i]) for i in range(len(command)) if i % 2]    # numbers only exist in odd indices
            commands.append(commandNumbers)


stacksCount = len((cargo.pop(-1)).split())    # last item of cargo is 1 2 3 ... n
stacks = []

for i in range(stacksCount):
    stack = deque()
    stacks.append(stack)

rowCargo = []

for str in cargo:
    rowCargo.append([str[i:i+3] for i in range(0, len(str), 4)])

for i in rowCargo[::-1]:
    j = 0
    while j < stacksCount:
        if i[j] != "   ":
            stacks[j].append(i[j])
        j += 1

for i in commands:
    num = i[0]
    src = i[1] - 1  # because lists are 0-based index
    dst = i[2] - 1  # because lists are 0-based index

    stacks[src], stacks[dst] = stack_move_multiple(stacks[src], stacks[dst], num)

for i in stacks:
    print(i.pop()[1], end = "")
