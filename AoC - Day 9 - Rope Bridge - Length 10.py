rope = {0: [0, 0],
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 0],
        8: [0, 0],
        9: [0, 0]}

def sign(num):
    if num == 0:
        return 0
    return num // abs(num)  # guaranteed to be 1 or -1

def tail_locator(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:     # check if tail is below two spaces away from head
        return tuple(tail)
    
    rMovement = sign(head[0] - tail[0])
    cMovement = sign(head[1] - tail[1])
    
    return [tail[0] + rMovement, tail[1] + cMovement]


visitedCoords = set()


with open('input9.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        command = i.split()
        match command[0]:
            case "U":
                rMovement, cMovement = 1, 0
            case "D":
                rMovement, cMovement = -1, 0
            case "L":
                rMovement, cMovement = 0, -1
            case "R":
                rMovement, cMovement = 0, 1

        for i in range(int(command[1])):
            rope[0][0] += rMovement
            rope[0][1] += cMovement
            for j in range(1, 10):
                rope[j] = tail_locator(rope[j - 1], rope[j])
                visitedCoords.add(tuple(rope[9]))

print(len(visitedCoords))