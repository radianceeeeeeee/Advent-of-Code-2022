import re

monkeys = {}

def parse_operation(arr, oldValue):     # equation parser
    if arr[0] == "old":
        a = oldValue
    else:
        a = int(arr[0])

    if arr[2] == "old":
        b = oldValue
    else:
        b = int(arr[2])

    if arr[1] == "+":
        return a + b
    elif arr[1] == "-":
        return a - b
    elif arr[1] == "*":
        return a * b
    else:
        return a / b


with open('input11.txt') as f:
    inp = f.readlines()

    i = 0
    while i < len(inp):
        # getting the important data on each line
        monkeyID = int(inp[i].rstrip(":\n").split()[1])
        items = list(map(int, re.split((": |, "), inp[i + 1].rstrip("\n"))[1:]))
        operation = inp[i + 2].rstrip("\n").split()[3:]
        test = int(inp[i + 3].rstrip("\n").split()[3])
        ifTrue = int(inp[i + 4].rstrip("\n").split()[5])
        ifFalse = int(inp[i + 5].rstrip("\n").split()[5])

        # initializing and appending the information on the monkey ID
        monkeys[monkeyID] = {}
        monkeys[monkeyID]["items"] = items
        monkeys[monkeyID]["operation"] = operation
        monkeys[monkeyID]["test"] = test
        monkeys[monkeyID]["ifTrue"] = ifTrue
        monkeys[monkeyID]["ifFalse"] = ifFalse
        monkeys[monkeyID]["inspectionsNum"] = 0

        # the input has 7 lines, newline included, per monkey
        i += 7

# this ensures that the worry levels won't reach integer limit
# what this code snippet does is to get the product of all test values
# so that all remainders regardless of all test value won't matter
worry_minimizer = 1
for i in monkeys.keys():
    worry_minimizer *= monkeys[i]["test"]


def round(monkeys):
    id = 0
    while id < len(monkeys.items()):
        monkeys[id]["inspectionsNum"] += len(monkeys[id]["items"])      # keeps track of inspection per monkey
        itemID = len(monkeys[id]["items"]) - 1
        while itemID >= 0:      # we check the items in reverse order so that popping the items won't mess the index of the list
            worry_level = parse_operation(monkeys[id]["operation"], monkeys[id]["items"][itemID]) % worry_minimizer
            monkeys[id]["items"].pop()      # pop the current item as it will be thrown to another monkey

            if worry_level % monkeys[id]["test"] == 0:
                monkeys[monkeys[id]["ifTrue"]]["items"].append(worry_level)
            else:
                monkeys[monkeys[id]["ifFalse"]]["items"].append(worry_level)
            
            itemID -= 1
        id += 1
    return monkeys

for i in range(10000):
    monkeys = round(monkeys)

inspections = []
for i in monkeys.keys():
    inspections.append(monkeys[i]["inspectionsNum"])

inspections.sort()
print(inspections[-1] * inspections[-2])    # gets the top two highest inspection count after sorting in ascending order