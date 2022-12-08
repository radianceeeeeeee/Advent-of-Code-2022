forest = []

# helper functions

def check_up_count(row, col, height, matrix):
    up = 0
    for i in range(row - 1, -1, -1):        # reverse order (starting from tree to edge)
        up += 1
        if matrix[row][col] <= matrix[i][col]:
            break
    return up

def check_down_count(row, col, height, matrix):
    down = 0
    for i in range(row + 1, height):        # no need to reverse
        down += 1
        if matrix[row][col] <= matrix[i][col]:
            break

    return down

def check_left_count(row, col, width, matrix):
    left = 0
    for j in range(col - 1, -1, -1):        # check left but in reverse order (starting from tree to edge)
        left += 1
        if matrix[row][col] <= matrix[row][j]:
            break
    return left

def check_right_count(row, col, width, matrix):
    right = 0
    for j in range(col + 1, width):         # check right (no need to reverse)
        right += 1
        if matrix[row][col] <= matrix[row][j]:
            break
    return right


# main function

def scenic_score(row, col, height, width, matrix):
    return check_up_count(row, col, height, matrix) * check_down_count(row, col, height, matrix) * check_left_count(row, col, width, matrix) * check_right_count(row, col, width, matrix)


with open('input8.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        forest.append(list(map(int, list(i.rstrip("\n")))))

height = len(forest)
width = len(forest[0])

highestScenicScore = 0

r = 0
while r < height:
    c = 0
    while c < width:
        highestScenicScore = max(highestScenicScore, scenic_score(r, c, height, width, forest))
        c += 1
    r += 1

print(highestScenicScore)