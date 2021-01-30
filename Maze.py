from types import DynamicClassAttribute
import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import colors

def mazeGen():

    maze = np.zeros((10,10))

    p = 0.3

    for x in np.nditer(maze, op_flags=['readwrite']):
        if random.random() <= p:
            x[...] = 1

    maze[0,0] = 0
    maze[9,9] = 0

    tuple1 = 0
    tuple2 = 0
    while (tuple1 == 0 and tuple2 == 0) or (tuple1 == 9 or tuple2 == 9):
        tuple1 = random.randint(1,9)
        tuple2 = random.randint(1,9)

        if maze[tuple1,tuple2] == 1:
            tuple1 = 0
            tuple2 = 0

    maze[tuple1,tuple2] = 2

    print(maze)

    plt.imshow(maze)
    plt.show()

def main():

    mazeGen()

if __name__ == "__main__":
    main()