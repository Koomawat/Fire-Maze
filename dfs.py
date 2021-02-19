from mazeGen import arrayToTree
import numpy as np
from collections import deque
import copy

def dfs(maze, start, goal, mlen):

    # keep a grid that marks where it was already explored
    visited = np.zeros((mlen, mlen))
    
    # DFS uses stack
    stack = deque()
    # starts at (0,0)
    stack.append(start)

    while stack:

        # current position
        x, y = stack.pop()
        
        # out of boundary, explore another position in stack
        if x >= mlen or y >= mlen or x < 0 or y < 0 or visited[x, y] == 1:
            continue

        # if it reached the goal, there is a path
        if (x, y) == goal:
            return True

        # skip if the cell is visited or blocked/fired
        if visited[x, y] == 1 or maze[x, y] >= 1:
            continue
        # if the cell is not visited and is empty
        elif visited[x, y] == 0 and maze[x, y] == 0:
            visited[x, y] = 1
                # stack right/down at last, because our goal is on the right bottom corner.
            stack.append((x-1, y))  # left
            stack.append((x, y-1))  # up
            stack.append((x, y+1))  # down
            stack.append((x+1, y))  # right
    
    return False

# for path marking
def dfs_graph(main_maze, start, goal, mlen):

    maze = copy.deepcopy(main_maze)

    # Initializes the stack with start cell (0,0) and no path yet
    stack = deque([[start, ""]])

    # keeps track of visited cells
    visited = set()

    # makes 2D array into graph
    tree = arrayToTree(maze)

    while stack:

        # current position traversing
        tuples = stack.pop()
        node, path = tuples

        (x, y) = node

        # if it reached the goal, return the path
        if node == goal:
            return path
        
        # if x, y out of boundar, ignore                                              
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue

        # if cell is blocked, ignore
        if maze[x, y] >= 1:
            continue
        # if cell is unvisited and empty, 
        # visit and add neighbor nodes and append path
        elif maze[x, y] == 0 and node not in visited:
            visited.add(node)
            for movement, neighborElements in tree[node]:
                # path = current path + new movement, doing it outside the append broke it randomly
                stack.append((neighborElements, path + movement))
    
    return "No such path from S to G exists"
    

    
