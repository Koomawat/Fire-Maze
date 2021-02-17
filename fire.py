import copy
import random
import math

# q value for flammability rate
def getQ():
    q = 0.1
    return q

def future_fire(maze):

    # creating a maze copy
    c_maze = copy.deepcopy(maze)

    # traversing each cell in the maze
    for y in range(len(c_maze)):
        for x in range(len(c_maze)):
            current = c_maze[x, y]

            # Flammability rate
            q = getQ()

            # If currently on a fire cell
            if (current == 2):
                
                # Set maze length
                mlen = len(c_maze)

                # If we go over bounds we ignore this if 
                if x + 1 >= mlen:
                    pass
                else:
                    if (c_maze[x+1, y] == 0):

                        # Future fire state cells are based on the q, 1 cell out for q <= 0.20
                        if q <= 0.20:
                            c_maze[x+1, y] = 4
                            if y+1 < mlen:
                                # bottom right cell of current fire
                                if c_maze[x+1, y+1] == 0:
                                    c_maze[x+1, y+1] = 4
                        # Future fire state cells are based on the q, 2 cells out for q > 0.20
                        else:
                            c_maze[x+1, y] = 4
                            # Checking if 2nd cell out is in bounds and is a free cell
                            if x + 2 >= mlen:
                                pass 
                            elif (c_maze[x+2, y] == 0 and c_maze[x+1, y] == 4):
                                c_maze[x+2, y] = 4
                            if y+1 < mlen:
                                # bottom right cell of current fire
                                if c_maze[x+1, y+1] == 0:
                                    c_maze[x+1, y+1] = 4

                # If we go over bounds we ignore this if 
                if x - 1 < 0:
                    pass
                else:
                    if (c_maze[x-1, y] == 0):

                        # Future fire state cells are based on the q, 1 cell out for q <= 0.20
                        if q <= 0.20:
                            c_maze[x-1, y] = 4
                            if y-1 >= 0:
                                # top right cell of current fire
                                if c_maze[x-1, y-1] == 0:
                                    c_maze[x-1, y-1] = 4
                        # Future fire state cells are based on the q, 2 cells out for q > 0.20
                        else:
                            c_maze[x-1, y] = 4
                            # Checking if 2nd cell out is in bounds and is a free cell
                            if x - 2 < 0:
                                pass 
                            elif (c_maze[x-2, y] == 0 and c_maze[x-1, y] == 4):
                                c_maze[x-2, y] = 4
                            if y-1 >= 0:
                                # top right cell of current fire
                                if c_maze[x-1, y-1] == 0:
                                    c_maze[x-1, y-1] = 4

                # If we go over bounds we ignore this if 
                if y + 1 >= mlen:
                    pass
                else:
                    if (c_maze[x, y+1] == 0):

                        # Future fire state cells are based on the q, 1 cell out for q <= 0.20
                        if q <= 0.20:
                            c_maze[x, y+1] = 4
                            if x-1 >= 0:
                                # top left cell of current fire
                                if c_maze[x-1, y+1] == 0:
                                    c_maze[x-1, y+1] = 4
                        # Future fire state cells are based on the q, 2 cells out for q > 0.20
                        else:
                            c_maze[x, y+1] = 4
                            # Checking if 2nd cell out is in bounds and is a free cell
                            if y + 2 >= mlen:
                                pass 
                            elif (c_maze[x, y+2] == 0 and c_maze[x, y+1] == 4):
                                c_maze[x, y+2] = 4
                            if x-1 >= 0:
                                # top left cell of current fire
                                if c_maze[x-1, y+1] == 0:
                                    c_maze[x-1, y+1] = 4

                # If we go over bounds we ignore this if 
                if y - 1 < 0:
                    pass
                else:
                    if (c_maze[x, y-1] == 0):

                        # Future fire state cells are based on the q, 1 cell out for q <= 0.20
                        if q <= 0.20:
                            c_maze[x, y-1] = 4
                            if x+1 < mlen:
                                # bottom left cell of current fire
                                if c_maze[x+1, y-1] == 0:
                                    c_maze[x+1, y-1] = 4
                        # Future fire state cells are based on the q, 2 cells out for q > 0.20
                        else:
                            c_maze[x, y-1] = 4
                            # Checking if 2nd cell out is in bounds and is a free cell
                            if y - 2 < 0:
                                pass 
                            elif (c_maze[x, y-2] == 0 and c_maze[x, y-1] == 4):
                                c_maze[x, y-2] = 4
                            if x+1 < mlen:
                                # bottom left cell of current fire
                                if c_maze[x+1, y-1] == 0:
                                    c_maze[x+1, y-1] = 4

    # returning the maze with potential future fire states indicated by the number 4 
    return c_maze

def spread_fire(maze, q):

    # copying mazes to not change original
    c_maze = copy.deepcopy(maze)
    result_maze = copy.deepcopy(maze)

    # traversing each cell in the maze
    for y in range(len(c_maze)):
        for x in range(len(c_maze)):
            # setting value of current cell
            current = c_maze[x, y]
            # we spread fire on cells if the current fire has free neighbors and the random probasbi
            if (current != 2 and current != 1):
                # k represents the number of fire neighbors of the current cell
                k = count_neighbor(c_maze, x, y)
                
                # probabilty = 1 - (1-q)^k
                prob = 1 - (math.pow((1 - q),k))
                # getting a number between 0 and 1
                rand = random.uniform(0, 1)
                # if random <= probabilty we set the cell to a fire state 
                if rand <= prob: 
                    result_maze[x, y] = 2
                    
    return result_maze

# function to find the number of fire state neighbors a cell has
def count_neighbor(maze, x, y):
    count = 0
    mlen = len(maze)

    if x + 1 >= mlen:
        pass
    elif maze[x+1, y] == 2:
        count += 1

    if x - 1 < 0:
        pass
    elif maze[x-1, y] == 2:
        count += 1

    if y + 1 >= mlen:
        pass
    elif maze[x, y+1] == 2:
        count += 1

    if y - 1 < 0:
        pass
    elif maze[x, y-1] == 2:
        count += 1

    return count
    

    
