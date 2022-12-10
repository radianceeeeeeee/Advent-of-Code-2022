x = 1
cycleNum = 1
totalSignalStrength = 0

def signal_strength(cycle, reg):
    if cycleNum % 40 == 20:
        return cycle * reg
    return 0

with open('input10.txt') as f:
    inp = f.readlines()

    for i in inp:
        command = i.split()
        
        totalSignalStrength += signal_strength(cycleNum, x)     # add signal strength
        cycleNum += 1       # one cycle delay for both noop and addx

        if command[0] == "addx":
            totalSignalStrength += signal_strength(cycleNum, x)      # add signal strength
            cycleNum += 1       # another cycle delay for addx

            x += int(command[1])


print(totalSignalStrength)