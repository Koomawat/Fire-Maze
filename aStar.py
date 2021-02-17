from heapq import heappop
from heapq import heappush
# heapq (also known as priority queue) citation: https://docs.python.org/3/library/heapq.html
import copy
from mazeGen import *
import math
from fire import *

def stratThreeAStar(maze, aStarPath, goal):

    spread_maze = maze

    pathCopy = aStarPath[0]
    currentPos = pathToPosition(pathCopy, 0, 0)

    mlen = len(spread_maze)

    count = 1


    if(aStarPath != "No such path from S to G exists."):

        while (currentPos != goal):

            x = currentPos[0]
            y = currentPos[1]
            
            if (x > mlen-1) or (y > mlen-1):
                break

            spread_maze = spread_fire(spread_maze)
            future_spread = future_fire(spread_maze)
            #print(pathCopy)
            #print(x,y)
            color_maze = singleColorPath(pathCopy, future_spread, x, y)
            plt.imshow(color_maze)
            plt.show()

            mlen = len(future_spread)

            if(spread_maze[x,y] == 2):
                response = "Agent died!"
                return response

            if (future_spread[x,y] == 4):
                aStarPath = aStar(future_spread, currentPos, goal)
                pathCopy = aStarPath[0]
                currentPos = pathToPosition(pathCopy, x, y)
                
                count = 1
                if(aStarPath == "No such path from S to G exists."):
                    return aStarPath

            else:
                pathCopy = aStarPath[count]
                currentPos = pathToPosition(pathCopy, x, y)
                x = currentPos[0]
                y = currentPos[1]
                count += 1

            

    else:
        response = "No such path from S to G exists."
        return response

    if (currentPos == goal):
        response = "Agent survived!"
        return response


def stratTwoAStar(maze, aStarPath, goal):

    spread_maze = maze
    pathCopy = aStarPath[0]
    currentPos = pathToPosition(pathCopy, 0, 0)

    if(aStarPath != "No such path from S to G exists."):
        while (currentPos != goal):

            x = currentPos[0]
            y = currentPos[1]

            spread_maze = spread_fire(spread_maze)

            if(spread_maze[x,y] == 2):
                response = "Agent died!"
                return response

            newAStarPath = aStar(spread_maze, currentPos, goal)

            if(newAStarPath == "No such path from S to G exists."):
                return newAStarPath

            pathCopy = newAStarPath[0]
            currentPos = pathToPosition(pathCopy, x, y)

            #color_maze = colorPath(newAStarPath, spread_maze, x, y)
            #plt.imshow(color_maze)
            #plt.show()
    else:
        response = "No such path from S to G exists."
        return response

    if (currentPos == goal):
        response = "Agent survived!"
        return response


def euclideanHeuristic(child, goal):
    # Using the euclidean metric but not having the square root as it will cost too much
    return abs(((child[0] - goal[0])**2) + ((child[1] - goal[1])**2))


def aStar(main_maze, start, goal):
    
    if(start == goal):
        return ""

    maze = copy.deepcopy(main_maze)

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
    
    # If path was not returned it and there's no longer a priority queue, no path from S to G was found
    return "No such path from S to G exists."