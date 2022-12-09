head = [0, 0]
tail = [0, 0]   # head covers tail initially

def sign(num):
    if num == 0:
        return 0
    return num // abs(num)  # guaranteed to be 1 or -1

def tail_locator(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:     # check if tail is below two spaces away from head
        return tuple(tail)
    
    rMovement = sign(head[0] - tail[0])
    cMovement = sign(head[1] - tail[1])
    
    return (tail[0] + rMovement, tail[1] + cMovement)


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
            head[0] += rMovement
            head[1] += cMovement
            tail = tail_locator(head, tail)
            visitedCoords.add(tail)

print(len(visitedCoords))