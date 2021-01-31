import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import colors

def mazeGen():

    maze_length = int(input("Enter the length of a square maze: "))
    # Hard coded dim x dim matrix to represent the Maze
    maze = np.zeros((maze_length, maze_length))
    

    # Variable p represents the probability of a cell in the Maze being occupied
    p = 0.3

    # Here we use numpy to traverse the Maze we created
    # For each cell we do a random from 0 to 1 and if the value is p or less the cell will have an occupied state
    for x in np.nditer(maze, op_flags=['readwrite']):
        if random.random() <= p:
            x[...] = 1

    # The first cell and the very last cell cannot be occupied as they are the start and end points of the Maze
    # For the Maze a free cell is represented as a 0
    # An occupied cell is represented as a 1
    # A fire cell is represented as a 2
    maze[0,0] = 0
    maze[9,9] = 0

    # Here we find a random free cell in the Maze for the initial fire position
    # tuple1, tuple2 represent the 
    tuple1 = 0
    tuple2 = 0
    # We don't want the tuples to be 0,0 or 9,9 as those cells are the start and end of the Maze
    while (tuple1 == 0 and tuple2 == 0) or (tuple1 == 9 or tuple2 == 9):
        tuple1 = random.randint(1,9)
        tuple2 = random.randint(1,9)

        # Checking if the tuples generated are an occupied cell
        # If so we reset the tuples to 0 so we keep looping until we find a random free cell
        if maze[tuple1,tuple2] == 1:
            tuple1 = 0
            tuple2 = 0

    # Setting the random tuple as the initial fire spot 
    maze[tuple1,tuple2] = 2

    # Using matplotlib to visualize the Maze in a grid view
    plt.imshow(maze)
    plt.show()

    return maze, maze_length
