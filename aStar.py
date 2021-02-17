import heapq
# heapq (also known as priority queue) citation: https://docs.python.org/3/library/heapq.html
import copy
from mazeGen import *
from fire import *

def stratThreeAStar(maze, aStarPath, goal, q, ogPath):
    # Copy of maze to call spread fire on
    spread_maze = maze

    # Retreiving first direction of movement from A* initial path
    pathCopy = aStarPath[0]
    
    
    # Converting current direction value to a tuple value
    currentPos = pathToPosition(pathCopy, 0, 0)

    # Length of the maze
    mlen = len(spread_maze)

    # Count will be used to traverse on calculated paths until we need to recalculate a path and count needs to be resetted
    count = 1

    # When a path exists from S to G
    if(aStarPath != "No such path from S to G exists."):

        # While the current tuple is not the goal tuple we keep looping
        while (currentPos != goal):

            # x,y to get respective tuple values from (x,y)
            x = currentPos[0]
            y = currentPos[1]
            
            # Bounds check for x and y
            if (x > mlen-1) or (y > mlen-1):
                break

            # Calling spread_fire to spread the fire at every step
            spread_maze = spread_fire(spread_maze, q)
            # Calling future_fire on spread_maze to get a future fire zone in the maze (indicated by a value of 4)
            future_spread = future_fire(spread_maze, q)

            # Plot testing code under to see each agent movement 1 by 1 as well as the fire/future fire spreading 
            # color_maze = singleColorPath(future_spread, x, y)

            ogPath += pathCopy
            # print(ogPath)
            # plt.imshow(color_maze)
            # plt.show()

            # If somehow the agent and fire meet on the same cell the agent will die 
            if(spread_maze[x,y] == 2):
                response = ogPath + pathCopy
                msg = "Agent died! b "
                # print(response)
                return response, msg, spread_maze

            # Bounds check for future fires
            if(x+1 < mlen and y+1 < mlen):
                # If a neighbor cell is a future fire cell state, we begin the path recomputation process
                if((future_spread[x+1,y] == 4) or (future_spread[x-1,y] == 4) or (future_spread[x,y+1] == 4) or (future_spread[x,y-1] == 4)):
                    
                    aStarPath_copy = aStarPath

                    # If somehow the agent is trapped between future fires states, we call the new path that goes through the future fire so the agent is not stuck
                    if (x+1 < mlen and y+1 < mlen and x-1 >= 0 and y-1 >= 0 
                    and future_spread[x+1, y] != 0) and (future_spread[x-1, y] != 0) and (future_spread[x, y+1] != 0) and (future_spread[x, y-1] != 0):
                        aStarPath = aStar(spread_maze, currentPos, goal)
                    # If not, the path recalculated starts from the closest free state cell (indicated by 0) to the goal
                    else:
                        aStarPath = aStar(future_spread, currentPos, goal)

                    # Setting the new direction value from the new calculated path
                    pathCopy = aStarPath[0]

                    # Converting new first direction to a tuple value 
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Finding the x,y of the new tuple value (x,y)
                    x = currentPos[0]
                    y = currentPos[1]
                    # Resetting the count back to 1 just incase if we do not need a path recalculation instantly 
                    count = 1

                    # If the newly returned path tells us not path exists then the Agent is trapped and can no longer reach the goal
                    if(aStarPath == "No such path from S to G exists."):
                        response = ogPath + pathCopy
                        msg = "Agent died! a"
                        # print(response)
                        return response, msg, spread_maze

                # If the current cell has no future fire state cells then we simply keep following the most recently calculated path
                else:
                    
                    # Setting value of the next direction 
                    pathCopy = aStarPath[count]

                    # Converting it into a tuple
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Setting the x, y of the tuple (x,y) we made
                    x = currentPos[0]
                    y = currentPos[1]
                    # Incrementing count by 1 if we keep following the same path so we get the next direction in line
                    count += 1

            else:
                # Another repeat of the what's above except here we are treating an edge case where the agent's only path was to a future fire state cell
                if(future_spread[x,y] == 4):
                   
                    aStarPath_copy = aStarPath

                    # If somehow the agent is trapped between future fires states, we call the new path that goes through the future fire so the agent is not stuck
                    if (x+1 < mlen and y+1 < mlen and x-1 >= 0 and y-1 >= 0 
                    and future_spread[x+1, y] < 0) and (future_spread[x-1, y] != 0) and (future_spread[x, y+1] != 0) and (future_spread[x, y-1] != 0):
                        aStarPath = aStar(spread_maze, currentPos, goal)
                    else:
                    # If not, the path recalculated starts from the closest free state cell (indicated by 0) to the goal
                        aStarPath = aStar(future_spread, currentPos, goal)

                    # Setting the new direction value from the new calculated path
                    pathCopy = aStarPath[0]

                    # Converting new first direction to a tuple value 
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Finding the x,y of the new tuple value (x,y)
                    x = currentPos[0]
                    y = currentPos[1]
                    # Resetting the count back to 1 just incase if we do not need a path recalculation instantly 
                    count = 1

                    # If the newly returned path tells us not path exists then the Agent is trapped and can no longer reach the goal
                    if(aStarPath == "No such path from S to G exists."):
                        response = ogPath + pathCopy
                        msg = "Agent died!c"
                        # print(response)
                        return response, msg, spread_maze

                # If the current cell has no future fire state cells then we simply keep following the most recently calculated path
                else:
                    
                    # Setting value of the next direction 
                    pathCopy = aStarPath[count]
                    
                    # Converting it into a tuple
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Setting the x, y of the tuple (x,y) we made
                    x = currentPos[0]
                    y = currentPos[1]
                    # Incrementing count by 1 if we keep following the same path so we get the next direction in line
                    count += 1
    
    # If the initial path found no successful path, we return that it's not possible to get from S to G
    else:
        response = ogPath + pathCopy
        msg = "No such path from S to G exists."
        # print(response)
        return response, msg, spread_maze

    # If the current position tuple is the goal tuple it means the agent made it from S to G!
    if (currentPos == goal):
        response = ogPath + pathCopy
        # color_maze = colorPath(response, spread_maze, 0, 0)
        # plt.imshow(color_maze)
        # plt.show()
        msg = "Agent survived!"
        return response, msg, spread_maze


def stratTwoAStar(maze, aStarPath, goal, q, ogPath):


    # Copy of maze to call spread fire on
    spread_maze = maze

    # Retreiving first direction of movement from A* initial path
    pathCopy = aStarPath[0]

    # Converting current direction value to a tuple value
    currentPos = pathToPosition(pathCopy, 0, 0)

    # When a path exists from S to G
    if(aStarPath != "No such path from S to G exists."):
        while (currentPos != goal):

            ogPath += pathCopy

            # x,y tuple values from current position
            x = currentPos[0]
            y = currentPos[1]

            # Spreading fire 1 step on the maze we are working with
            spread_maze = spread_fire(spread_maze, q)

            # If the fire spreads onto the agent they die 
            if(spread_maze[x,y] == 2):
                response = ogPath + pathCopy
                msg = "Agent died! b "
                # print(response)
                return response, msg, spread_maze

            # Finding the new path after every time step
            newAStarPath = aStar(spread_maze, currentPos, goal, q)

            # If the newly returned path tells us not path exists then the Agent is trapped and can no longer reach the goal
            if(newAStarPath == "No such path from S to G exists."):
                response = ogPath + pathCopy
                msg = newAStarPath
                # print(response)
                return response, msg, spread_maze

            # Setting value of the new direction from the new path
            pathCopy = newAStarPath[0]
            # Converting the new direction into a tuple value
            currentPos = pathToPosition(pathCopy, x, y)

    # If the initial path found no successful path, we return that it's not possible to get from S to G
    else:
        response = ogPath + pathCopy
        msg = "No such path from S to G exists."
        # print(response)
        return response, msg, spread_maze

    # If the current position tuple is the goal tuple it means the agent made it from S to G!
    if (currentPos == goal):
        response = ogPath + pathCopy
        msg = "Agent survived!"
        # print(response)
        return response, msg, spread_maze


def euclideanHeuristic(child, goal):
    # Using the euclidean metric but not having the square root as it will cost too much
    return abs(((child[0] - goal[0])**2) + ((child[1] - goal[1])**2))


def aStarPush(priorityQ, item):
    # Push item into the priority queue
    return heapq.heappush(priorityQ, item)
    

def aStarPop(priorityQ):
    # Pop given heuristic cost, current key, and path from the priority queue
    return heapq.heappop(priorityQ)


def aStarNeighbors(tree, currKey, path, heuristicCost, goal, priorityQ):
    for movement, neighborElements in tree[currKey]:
            # Since we are working in a maze we can assume that each move left right up or down has a cost of 1
            newPath = path + movement
            # Updating the heap item with the new heuristic, new cost, new neighbors, and the updated optimal path
            itemUpdate = (heuristicCost + euclideanHeuristic(neighborElements, goal), heuristicCost+1 , neighborElements, newPath)
            # Pushing the new item into the heap
            aStarPush(priorityQ, itemUpdate)


def aStar(main_maze, start, goal):
    
    if(start == goal):
        return ""

    maze = copy.deepcopy(main_maze)

    # Initializing priority queue list/heap
    priorityQueue = []
    
    # Using a set called VisitedSet to keep tracked of the keys we will visit in the tree
    visitedSet = set()

    # Using heapq a.k.a. priority queue 
    # priorityQueue is the heap
    # The item of the heap is the heuristic, start cost, current element / tree key value, path to the goal
    item = (euclideanHeuristic(start, goal), 0, start, "")
    aStarPush(priorityQueue, item)

    # Converting the 2D array into a tree like dictionary structure
    tree = arrayToTree(maze)

    # We keep looping as long there is an item in the heap/priority queue
    while priorityQueue:
        
        # Working with the current heuristic, looking at the current cost, setting the path, and tracking current
        currHeuristic, heuristicCost, currentKey, path = aStarPop(priorityQueue)

        # Checking if current element in the tree is our goal state / node and if so we retun the path
        if currentKey == goal:
            return path

        # If the current key was already visited we go to the next item in the priority queue by passing (do nothing)
        elif currentKey in visitedSet:
            pass

        else:
            # We didn't visit this node yet and we didn't reach the goal so we add the current node/key to the visited set
            visitedSet.add(currentKey)

            # Retreiving current cell's neighbors from the dictionary/tree we made and pushing it into the priority queue for potential paths
            aStarNeighbors(tree, currentKey, path, heuristicCost, goal, priorityQueue)
    
    # If path was not returned it and there's no longer items in the priority queue, no path from S to G was found
    return "No such path from S to G exists."

