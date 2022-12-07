from treelib import Tree, Node

tree = Tree()
tree.create_node(0, "/")
currentNode = "/"
isCollectingNode = False

with open('input7.txt') as f:
    inp = f.readlines()
    
    for i in inp:        
        if i[:4] == "$ cd":
            isCollectingNode = False
            tempNode = i.split()[2]  # by getting the element at index 2 of $ cd ___, we will get the directory
            if tempNode == "..":
                currentNode = tree.parent(currentNode).identifier   # if you step back, the parent is now the current node
            elif tempNode != "/":
                currentNode = currentNode + "\\" + tempNode     # otherwise, you are accessing a deeper folder which is current node + directory name
        elif isCollectingNode:      # used for collecting children nodes
            command = i.split()
            if command[0] == "dir": 
                value = 0   # if dir ___, instantiate file size as 0 initially
            else:   # otherwise, it's a file
                value = int(command[0]) # file size is at index 0

                parentNode = currentNode
                while parentNode != "/":    #  we will recursively add the filesize of the file on all ancestor folders
                    tree.get_node(parentNode).tag = int(tree.get_node(parentNode).tag) + value
                    parentNode = tree.parent(parentNode).identifier
                tree.get_node(parentNode).tag = int(tree.get_node(parentNode).tag) + value  # one more to add the filesize of root folder

            id = tree.get_node(currentNode).identifier + "\\" + command[1]  # file name is current folder + file name at index 1
            tree.create_node(value, id, currentNode)    # create new node with current folder as the parent folder
        elif i.rstrip("\n") == "$ ls":  # $ ls is a sign to collect succeeding lines as the children nodes of the current node
            isCollectingNode = True

#tree.show(line_type = "ascii", idhidden = False)

totalSpace = 70000000
usedSpace = totalSpace - tree.get_node("/").tag
minimum = totalSpace

for node in tree.expand_tree(mode = tree.DEPTH):
    if usedSpace + tree.get_node(node).tag > 30000000 and not tree[node].is_leaf():    # check if deleting it will result to 30000000 
        minimum = min(tree.get_node(node).tag, minimum)                                 # and if it's a leaf which signifies empty folder or a file

print(minimum)