forest = []

# helper functions

def check_vert(row, col, height, matrix):
    for i in range(0, row):             # check up
        if matrix[row][col] <= matrix[i][col]:
            break
        elif i == row - 1:
            return True

    for i in range(row + 1, height):    # check down
        if matrix[row][col] <= matrix[i][col]:
            break
        elif i == height - 1:
            return True 
    return False

def check_hor(row, col, width, matrix):
    for j in range(0, col):             # check left
        if matrix[row][col] <= matrix[row][j]:
            break
        elif j == col - 1:
            return True

    for j in range(col + 1, width):     # check right
        if matrix[row][col] <= matrix[row][j]:
            break
        elif j == width - 1:
            return True 
    return False


# main function

def is_visible(row, col, height, width, matrix):
    if row == 0 or row == height - 1 or col == 0 or col == width - 1:
        return True
    elif check_vert(row, col, height, matrix) or check_hor(row, col, width, matrix):
        return True
    return False


with open('input8.txt') as f:
    inp = f.readlines()
    
    for i in inp:
        forest.append(list(map(int, list(i.rstrip("\n")))))

height = len(forest)
width = len(forest[0])

visibleTrees = 0

r = 0
while r < height:
    c = 0
    while c < width:
        if is_visible(r, c, height, width, forest):
            visibleTrees += 1
        c += 1
    r += 1

print(visibleTrees)
