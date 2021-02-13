import numpy as np
from collections import deque
from mazeGen import *
import mazeGen
import copy

# take the maze, start, goal, and length of one side as parameters
# marking visited nodes as 1 but could also just use a visited set and add the nodes as it traverses
def bfs(main_maze, start, goal, mlen):

    maze = copy.deepcopy(main_maze)

    # Initialize the queue and set the start and empty path string
    queue = deque([[start, ""]])

    # create a visited set (interchangable with list) 
    visited = set()

    # Convert the 2D array into a dictionary
    tree = arrayToTree(maze)

    while queue:

        tuples = (values) = queue.popleft()
        node, path = tuples
        #print(node)
        #print(currVal)
        #print(path) # doesn't print cuz empty

        (x, y) = node
        # if the goal is found, return true for now -> need to figure out what to do with display
        if node == goal:
            return path

        # keep getting an out of bounds axis error
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue

         # if the node is blocked or on fire, skip it and move on
        if maze[x, y] >= 1:
            continue

         # if the node is empty and hasnt been visited yet, add its neighbours to the queue
        elif maze[x, y] == 0 and node not in visited:
            visited.add(node) # mark it as visited by adding to the set
            for movement, neighborElements in tree[node]:
                # path = path + movement
                queue.append((neighborElements, path+movement))
            #node = (x+1, y)
            #path = newPath
            #tuples = node, path
            #queue.append(tuples) # add right
            #node = (x, y+1)
            #tuples = node, path
            #queue.append(tuples) # add down
            #node = (x, y-1)
            #tuples = node, path
            #queue.append(tuples) # add up
            #node = (x-1, y)
            #tuples = node, path
            #queue.append(tuples) # add left

    return "No such path from S to G exists" # filler for now