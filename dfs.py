import numpy as np
from collections import deque

def dfs(maze, start, goal, mlen):

    visited = np.zeros((mlen, mlen))
    visited[0, 0], visited[mlen-1, mlen-1] = 1, 1
    stack = deque()
    stack.append(start)

    while stack:

        x, y = stack.pop()

        if x >= mlen or y >= mlen or x < 0 or y < 0 or visited[x, y] == 1:
            continue;

        if (x, y) == goal:
            return True

        # skip if the cell is visited or blocked/fired
        if visited[x, y] == 1 or maze[x, y] >= 1:
            continue;
        elif visited[x, y] == 0 and maze[x, y] == 0:
            visited[x, y] = 1
                # stack right/down at last, because our goal is on the right bottom corner.
            stack.append((x-1, y))  # left
            stack.append((x, y-1))  # up
            stack.append((x, y+1))  # down
            stack.append((x+1, y))  # right
    
    return False

    

    
