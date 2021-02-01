from heapq import heappop
from heapq import heappush
from matplotlib import pyplot as plt
from matplotlib import colors

def arrayToTree(maze):

    # Converting a 2D numpy matrix into a "tree" like structure in using dictionaries
    dim = len(maze)

    # Setting the key of the dictionary to be the element location in the matrix
    tree = {(x, y): 
    # Values only set for elements where there is a free cell 
    # Occupied cells (represented by 1) and fire cells (represented by 2) are ignored
    []  for y in range(dim) 
            for x in range(dim) 
                if not (maze[x,y] == 1 or maze[x,y] == 2)}

    # Calling the neighbor function to set 
    return setNeighbors(tree,maze)

def setNeighbors(tree,maze):

    dim = len(maze)

    # Traversing for each key (or in other words 2d array element) in the tree dictionary and checking valid neighbors
    for x, y in tree.keys():
        
        # Neighbors can only be Down(D) or Right(R) if x,y is top left corner
        if(x == 0 and y == 0):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Up(U) or Right(R) if x,y is bottom left corner
        elif(x == (dim - 1) and y == 0):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))

        # Neighbors can only be Down(U) or Left(L) if x,y is top right corner
        elif(x == 0 and y == (dim - 1)):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U) or Left(L) if x,y is bottom right corner
        elif(x == (dim - 1) and y == (dim - 1)):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Left(L) on the upper edge
        elif(x == 0 and y != (0) and (y < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Up(U), Right(R) or Left(L) on the bottom edge
        elif(x == (dim - 1) and y != (0) and (y < (dim - 1))):
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))

        # Neighbors can only be Down(D), Right(R) or Up(U) on the left edge 
        elif(y == 0 and x != (0) and (x < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x, y - 1)))

        # Neighbors can only be Down(D), Left(L) or Up(U) on the right edge 
        elif(y == (dim - 1) and x != (0) and (x < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))

        # Neighbors can be Down(D), Right(R), Left(L), or Up(U) on not edges
        elif(x != (0) and (x < (dim - 1)) and y != (0) and (y < (dim - 1))):
            if(maze[x+1,y] == 0):
                tree[(x, y)].append(("D", (x + 1, y)))
            if(maze[x,y+1] == 0):
                tree[(x, y)].append(("R", (x, y + 1)))
            if(maze[x,y-1] == 0):
                tree[(x, y)].append(("L", (x, y - 1)))
            if(maze[x-1,y] == 0):
                tree[(x, y)].append(("U", (x - 1, y)))

    # Test to print dictionary
    #for k,v in tree.items():
        #print(k, ' : ', v)

    return tree


def euclideanHeuristic(child, goal):
    # Using the euclidean metric but not having the square root as it will cost too much
    return ((child[0] - goal[0])**2) + ((child[1] - goal[1])**2)


def aStar(maze, start, goal):
    
    # Initializing priority queue list/heap
    priorityQueue = []
    
    # Visited set to keep tracked of the keys we will visit in the tree
    visitedSet = set()

    # Using heapq a.k.a. priority queue 
    # priorityQueue is the heap
    # The item of the heap is the heuristic, start cost, current element / tree key value, path to the goal
    item = (euclideanHeuristic(start, goal), 0, start, "")
    heappush(priorityQueue, item)

    # Converting the 2D array into a tree like dictionary structure
    tree = arrayToTree(maze)

    # We keep looping as long there is an item in the heap/priority queue
    while priorityQueue:

        # Working with the current heuristic, looking at the current cost, setting the path, and tracking current
        currHeuristic, huristicCost, currentKey, path = heappop(priorityQueue)

        # Checking if current element in the tree is our goal state / node and if so we retun the path
        if currentKey == goal:
            return path

        # If the current key was already visited we go to the next item in the priority queue
        if currentKey in visitedSet:
            continue
        
        # We didn't visit this node yet and we didn't reach the goal so we add the current node/key to the visited set
        visitedSet.add(currentKey)

        for movement, neighborElements in tree[currentKey]:
            # Since we are working in a maze we can assume that each move left right up or down has a cost of 1
            newPath = path + movement
            # Updating the heap item with the new heuristic, new cost, new neighbors, and the updated optimal path
            itemUpdate = (huristicCost + euclideanHeuristic(neighborElements, goal), huristicCost+1 , neighborElements, newPath)
            heappush(priorityQueue, itemUpdate)
    
    return "No such path from S to G exists."
