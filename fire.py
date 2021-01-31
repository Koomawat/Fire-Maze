import copy
import random

def spread_fire(maze):

    c_maze = copy.deepcopy(maze)

    for y in c_maze:
        for x in y:
            current = c_maze[x, y]
            if current != 2 and current != 1:
                k =  count_neighbor(c_maze, x, y)
                q = random.randint(0, 1)
                prob = 1 - (1 - q) ** k

                if random.randint(0, 1) <= prob:
                    c_maze[x, y] = 2

    return c_maze

def count_neighbor(maze, x, y):
    count = 0

    if maze[x+1, y] == 2:
        count += 1
    if maze[x-1, y] == 2:
        count += 1
    if maze[x, y+1] == 2:
        count += 1
    if maze[x, y-1] == 2:
        count += 1

    return count
    

    
