import numpy as np
from collections import deque
from matplotlib import pyplot as plt
from matplotlib import colors
from mazeGen import *
import mazeGen

# take the maze, start, goal, and length of one side as parameters
# marking visited nodes as 1 but could also just use a visited set and add the nodes as it traverses
def bfs(maze, start, goal, mlen):

    # Initialize the queue and set the start in
    queue = deque([[start, 0, ""]])

    # create a visited list (interchangable with set) 
    visited = np.zeros((mlen, mlen))

    # Convert the 2D array into a dictionary
    tree = arrayToTree(maze)

    while queue:

        tuples = (values) = queue.popleft()
        node, currVal, path = tuples
        print(node)
        print(currVal)
        print(path) # doesn't print cuz empty

        # node = (x, y)
        # # if the goal is found, return true for now -> need to figure out what to do with display
        # if(x, y) == goal:
        #     return path

        # # keep getting an out of bounds axis error
        # if x >= mlen or y >= mlen or x < 0 or y < 0:
        #     continue

        # # if the node is blocked, on fire, or already visited, skip it and move on
        # if maze[x, y] >= 1 or visited[x, y] == 1:
        #     continue

        # # if the node is empty and hasnt been visited yet, add its neighbours to the queue with right/down prio
        # elif maze[x, y] == 0 and visited[x, y] == 0:
        #     visited[x, y] = 1 # mark it as visited (may need to change)
        #     for movement, neighborElements in tree[node]:
        #         newPath = path + movement
        #     queue.append((x+1, y), newPath) # add right
        #     queue.append((x, y+1), newPath) # add down
        #     queue.append((x, y-1), newPath) # add up
        #     queue.append((x-1, y), newPath) # add left

    return False # filler for now

