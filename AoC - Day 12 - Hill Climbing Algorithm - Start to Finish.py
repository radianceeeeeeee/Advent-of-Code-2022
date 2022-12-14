from collections import deque

maze = []

with open('input12.txt') as f:
    inp = f.readlines()

    for i in inp:
        maze.append(list(i.rstrip("\n")))

def symbol_finder(grid, symbol):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)

startingPoint = symbol_finder(maze, "S")
maze[startingPoint[0]][startingPoint[1]] = "`"
finishPoint = symbol_finder(maze, "E")
maze[finishPoint[0]][finishPoint[1]] = "z"
shortestPathLength = len(maze) * len(maze[0])    # the default shortest path length will be the size of the maze

def grid_dict(defaultValue, height, width):
    dict = {}
    for i in range(height):
        for j in range(width):
            dict[(i, j)] = defaultValue
    return dict

def next_paths(grid, row, col):
    adjacentNodes = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for i in range(len(adjacentNodes) - 1, -1, -1):
        if adjacentNodes[i][0] < 0 or adjacentNodes[i][0] > len(grid) - 1:
            adjacentNodes.pop(i)
            continue

        if adjacentNodes[i][1] < 0 or adjacentNodes[i][1] > len(grid[0]) - 1:
            adjacentNodes.pop(i)
            continue

        if ord(grid[adjacentNodes[i][0]][adjacentNodes[i][1]]) - ord(grid[row][col]) > 1:
            adjacentNodes.pop(i)

    return adjacentNodes


def bfs(grid, start, finish, pred, dist):
    queue = deque()

    row, col = start

    queue.append((row, col))
    visitedPaths = grid_dict(False, len(maze), len(maze[0]))
    visitedPaths[(row, col)] = True
    dist[(row, col)] = 0

    while queue:
        currentCoords = queue.popleft()
        for i in next_paths(grid, currentCoords[0], currentCoords[1]):
            if not visitedPaths[i]:
                queue.append(i)
                visitedPaths[i] = True
                pred[i] = currentCoords
                dist[i] = dist[(currentCoords)]
                if (i[0], i[1]) == finish:
                    return True

    return False


def shortest_path(grid, start, finish):
    predecessors = grid_dict([], len(grid), len(grid[0]))
    distance = grid_dict(shortestPathLength, len(grid), len(grid[0]))

    if not bfs(grid, start, finish, predecessors, distance):
        return -1

    path = []
    crawl = finish
    ctr = 1

    gridprint = [[" " for _ in range(len(grid[0]))] for _ in range(len(grid))]    

    while predecessors[crawl] != start:
        gridprint[crawl[0]][crawl[1]] = maze[crawl[0]][crawl[1]]
        path.append(predecessors[crawl])
        crawl = predecessors[crawl]
        ctr += 1

    return ctr

print(shortest_path(maze, startingPoint, finishPoint))