rocks = set()
sands = set()

# this function is made so that range it will work when a > b in range(a, b)
def custom_range(x, y, inclusive = False) -> range:
    if x > y:
        if inclusive:
            return range(y, x + 1)
        return range(y, x)

    if inclusive:
        return range(x, y + 1)
    return range(x, y)

# setup function to pinpoint all rocks in a grid
def rock_maker(rockCorners: list) -> list:
    rocks = set()

    rockCornerA = tuple(map(int, rockCorners[0].split(",")))

    for i in rockCorners[1:]:
        rockCornerB = tuple(map(int, i.split(",")))

        if rockCornerA[0] == rockCornerB[0]:
            for j in custom_range(rockCornerA[1], rockCornerB[1], True):
                rocks.add((rockCornerA[0], j))
        elif rockCornerA[1] == rockCornerB[1]:
            for j in custom_range(rockCornerA[0], rockCornerB[0], True):
                rocks.add((j, rockCornerA[1]))

        rockCornerA = rockCornerB

    return rocks

# main function
def sand_fall(rocksCoords: set, sandsCoords: set, sandSourceCoords: tuple) -> set:
    sandCoords = sandSourceCoords
    
    maxY = -1
    for i in rocksCoords:
        maxY = max(i[1], maxY)


    while sandCoords[1] < maxY:
        if ((sandCoords[0], sandCoords[1] + 1) not in rocksCoords) and ((sandCoords[0], sandCoords[1] + 1) not in sandsCoords):
            sandCoords = (sandCoords[0], sandCoords[1] + 1)
            continue
        elif ((sandCoords[0] - 1, sandCoords[1] + 1) not in rocksCoords) and ((sandCoords[0] - 1, sandCoords[1] + 1) not in sandsCoords):
            sandCoords = (sandCoords[0] - 1, sandCoords[1] + 1)
            continue
        elif ((sandCoords[0] + 1, sandCoords[1] + 1) not in rocksCoords) and ((sandCoords[0] + 1, sandCoords[1] + 1) not in sandsCoords):
            sandCoords = (sandCoords[0] + 1, sandCoords[1] + 1)
            continue
        else:
            return sandsCoords.union({sandCoords})

# helper function, counts how many times until succeeding sands fall of the ground
def sand_tick(rocksCoords: set, sandsCoords: set, sandSourceCoords: tuple) -> int:
    prevSet = sandsCoords
    nextSet = sand_fall(rocksCoords, sandsCoords, sandSourceCoords)

    tick = 0
    while nextSet != None:
        prevSet = nextSet
        nextSet = sand_fall(rocksCoords, prevSet, sandSourceCoords)        
        tick += 1

    return tick


with open('input14.txt') as f:
    inp = f.readlines()
    for i in inp:
        rockDim = i.rstrip("\n").split(" ->")

        rocks.update(rock_maker(rockDim))

sandCoords = (500, 0)

print(sand_tick(rocks, sands, sandCoords))