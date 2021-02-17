from mazeGen import arrayToTree
import numpy as np
from collections import deque
import copy

def dfs(maze, start, goal, mlen):

    visited = np.zeros((mlen, mlen))
    stack = deque()
    stack.append(start)

    str = ''

    while stack:

        # need to work with graph

        x, y = stack.pop()
        
        # str += current

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

def dfs_graph(main_maze, start, goal, mlen):

    maze = copy.deepcopy(main_maze)

    stack = deque([[start, ""]])

    visited = set()

    tree = arrayToTree(maze)

    while stack:
        tuples = (values) = stack.pop()
        node, path = tuples

        (x, y) = node
        if node == goal:
            return path
        
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue

        if maze[x, y] >= 1:
            continue

        elif maze[x, y] == 0 and node not in visited:
            visited.add(node)
            for movement, neighborElements in tree[node]:
                # path = path + movement
                stack.append((neighborElements, path + movement))

    
    return "No such path from S to G exists"
    

    
