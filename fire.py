import copy
import random

from matplotlib import pyplot as plt
from matplotlib import colors

def spread_fire(maze):
    c_maze = copy.deepcopy(maze)

    for y in range(len(c_maze)):
        y = int(y)
        for x in range(len(c_maze)):
            x = int(x)
            current = c_maze[y, x]
            if current != 2 and current != 1:
                k =  count_neighbor(c_maze, x, y)
                q = random.randint(0, 1)
                prob = 1 - ((1 - q) ** k)

                if random.randint(0, 1) <= prob:
                    c_maze[y, x] = 2

    return c_maze

def count_neighbor(maze, x, y):
    count = 0

    try: 
        if maze[x+1, y] == 2:
            count += 1
    except:
        pass

    try:
        if maze[x-1, y] == 2:
            count += 1
    except:
        pass

    try:
        if maze[x, y+1] == 2:
            count += 1
    except:
        pass

    try:
        if maze[x, y-1] == 2:
            count += 1
    except:
        pass

    return count
    

    
