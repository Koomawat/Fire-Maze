import numpy as np
import random
import copy
from matplotlib import pyplot as plt
from matplotlib import colors

def mazeGen():

    # Taking size of the maze from the user
    maze_length = int(input("Enter the length of a square maze: "))
    maze = np.zeros((maze_length, maze_length))

    # Variable p represents the probability of a cell in the Maze being occupied
    p = 0.2

    # Here we use numpy to traverse the Maze we created
    # For each cell we do a random from 0 to 1 and if the value is p or less the cell will have an occupied state
    for x in np.nditer(maze, op_flags=['readwrite']):
        rand = random.random()

        # random.random() generates a number in [0, 1)
        # random generate a number until it excludes 0 too
        while (rand == 0):
            rand = random.random()

        if (rand <= p):
            x[...] = 1

    # The first cell and the very last cell cannot be occupied as they are the start and end points of the Maze
    # For the Maze a free cell is represented as a 0
    # An occupied cell is represented as a 1
    # A fire cell is represented as a 2
    maze[0,0] = 0
    maze[maze_length-1,maze_length-1] = 0

    # Here we find a random free cell in the Maze for the initial fire position
    # tuple1, tuple2 represent the 
    tuple1 = 0
    tuple2 = 0
    # We don't want the tuples to be 0,0 or length-1,length-1 as those cells are the start and end of the Maze
    while (tuple1 == 0 and tuple2 == 0) or (tuple1 == (maze_length-1) and tuple2 == (maze_length-1)):
        tuple1 = random.randint(1,maze_length-1)
        tuple2 = random.randint(1,maze_length-1)

        # Checking if the tuples generated are an occupied cell
        # If so we reset the tuples to 0 so we keep looping until we find a random free cell
        if maze[tuple1,tuple2] == 1:
            tuple1 = 0
            tuple2 = 0

    # Setting the random tuple as the initial fire spot 
    maze[tuple1,tuple2] = 2

    return maze, maze_length

def arrayToTree(maze):
    
    # Converting a 2D numpy matrix into a "tree" like structure in using dictionaries
    dim = len(maze)

    # Setting the key of the dictionary to be the element location in the matrix
    tree = {(x, y): 
    # Values only set for elements where there is a free cell 
    # Occupied cells (represented by 1) and fire cells (represented by 2) are ignored
    []  for y in range(dim) 
            for x in range(dim) 
                if not (maze[x,y] == 1 or maze[x,y] == 2)}

    # Calling the neighbor function to set 
    return setNeighbors(tree,maze)

def setNeighbors(tree,maze):

    dim = len(maze)

    # Traversing for each key (or in other words 2d array element) in the tree dictionary and checking valid neighbors
    for x, y in tree.keys():
        
        # Neighbors can only be Down(D) or Right(R) if x,y is top left corner
        if(x == 0 and y == 0):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Up(U) or Right(R) if x,y is bottom left corner
        elif(x == (dim - 1) and y == 0):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Down(U) or Left(L) if x,y is top right corner
        elif(x == 0 and y == (dim - 1)):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U) or Left(L) if x,y is bottom right corner
        elif(x == (dim - 1) and y == (dim - 1)):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Left(L) on the upper edge
        elif(x == 0 and y != (0) and (y < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U), Right(R) or Left(L) on the bottom edge
        elif(x == (dim - 1) and y != (0) and (y < (dim - 1))):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Up(U) on the left edge 
        elif(y == 0 and x != (0) and (x < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x-1, y)))

        # Neighbors can only be Down(D), Left(L) or Up(U) on the right edge 
        elif(y == (dim - 1) and x != (0) and (x < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))

        # Neighbors can be Down(D), Right(R), Left(L), or Up(U) on not edges
        elif(x != (0) and (x < (dim - 1)) and y != (0) and (y < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))

    # Test to print dictionary
    # for k,v in tree.items():
    #     print(k, ' : ', v)

    return tree

def colorPath(path, main_maze, y, x): 
    
    maze = copy.deepcopy(main_maze)

    # color in start position
    maze[y, x] = 3

    mlen = len(maze)
    

    for letter in path:
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            break

        if letter == "R":
            x += 1
        elif letter == "L":
            x -= 1
        elif letter == "U":
            y -= 1
        elif letter == "D":
            y += 1
        # [row, col]
        maze[y, x] = 3

    return maze
    
def pathToPosition(position, x, y):
    
    posCopy = position

    for element in posCopy:
        if(element == 'D'):
            x = x+1
        if(element == 'R'):
            y = y+1
        if(element == 'U'):
            x = x-1
        if(element== 'L'):
            y = y-1

    return (x,y)