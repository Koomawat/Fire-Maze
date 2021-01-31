import numpy as np
from collections import deque

# take the maze, start, goal, and length of one side as parameters
def bfs(maze, start, goal, mlen):
    queue = deque([start])
    visited = np.zeros((mlen, mlen))
    while queue:

        x, y = queue.pop()

        # if the goal is found, return true for now -> need to figure out what to do with display
        if(x, y) == goal:
            return True

        # if the node is blocked or is on fire skip it and move on + if its visited already
        if maze[x, y] >= 1 or visited[x, y] == 1:
            continue

        # if the node is empty and hasnt been visited yet, add its neighbours to the queue
        elif maze[x, y] == 0 and visited[x, y] == 0:
            visited[x, y] = 1
            # add right
            # add down
            # add up
            # add left

    return True # filler for now

