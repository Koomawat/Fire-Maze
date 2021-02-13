import copy
import random
import math

def spread_fire(maze):

    tupleTrack = []

    c_maze = copy.deepcopy(maze)

    for y in range(len(c_maze)):
        for x in range(len(c_maze)):
            current = c_maze[x, y]
            if (current != 2 and current != 1):
                k = count_neighbor(c_maze, x, y)
                q = random.uniform(0, 1)
                prob = 1 - (math.pow((1 - q),k))

                initialFire = True


                if ((x,y) in tupleTrack):
                    initialFire = False

                rand = random.uniform(0, 1)

                if ((rand <= prob) and (initialFire == True)):
                    c_maze[x, y] = 2
                    tupleTrack.append((x,y))
                    
    return c_maze

def count_neighbor(maze, x, y):
    count = 0

    try: 
        #print("reach1")
        if maze[x+1, y] == 2:
            count += 1
    except:
        pass

    try:
        #print("reach2")
        if maze[x-1, y] == 2:
            count += 1
    except:
        pass

    try:
        #print("reach3")
        if maze[x, y+1] == 2:
            count += 1
    except:
        pass

    try:
        #print("reach4")
        if maze[x, y-1] == 2:
            count += 1
    except:
        pass

    return count
    

    
