import numpy as np
from collections import deque
from mazeGen import *
import mazeGen
import copy
from fire import *


def stratThreeBfs(maze, optimalPath, goal, mlen, q):

    # Copy of maze to call spread fire on
    spread_maze = maze

    # Retreiving first direction of movement from bfs initial path
    pathCopy = optimalPath[0]

    # Converting current direction value to a tuple value
    currentPos = pathToPosition(pathCopy, 0, 0)

    # Count will be used to traverse on calculated paths until we need to recalculate a path and count needs to be resetted
    count = 1

    # When a path exists from S to G
    if(optimalPath != "No such path from S to G exists."):

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
            future_spread = future_fire(spread_maze)

            # If somehow the agent and fire meet on the same cell the agent will die 
            if(spread_maze[x,y] == 2):
                response = "Agent died!"
                return response

            # Bounds check for future fires
            if(x+1 < mlen and y+1 < mlen):
                # If a neighbor cell is a future fire cell state, we begin the path recomputation process
                if((future_spread[x+1,y] == 4) or (future_spread[x-1,y] == 4) or (future_spread[x,y+1] == 4) or (future_spread[x,y-1] == 4)):
                    
                    # If somehow the agent is trapped between future fires states, we call the new path that goes through the future fire so the agent is not stuck         
                    if (future_spread[x+1, y] != 0) and (future_spread[x-1, y] != 0) and (future_spread[x, y+1] != 0) and (future_spread[x, y-1] != 0):
                        optimalPath = bfs(spread_maze, currentPos, goal, mlen)
                    # If not, the path recalculated starts from the closest free state cell (indicated by 0) to the goal 
                    else:
                        optimalPath = bfs(future_spread, currentPos, goal, mlen)

                    # Setting the new direction value from the new calculated path
                    pathCopy = optimalPath[0]
                    # Converting new first direction to a tuple value 
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Finding the x,y of the new tuple value (x,y)
                    x = currentPos[0]
                    y = currentPos[1]
                    # Resetting the count back to 1 just incase if we do not need a path recalculation instantly 
                    count = 1
                    if(optimalPath == "No such path from S to G exists."):
                        optimalPath = f"No such path from {x}, {y} to G exists."
                        return optimalPath

                # If the current cell has no future fire state cells then we simply keep following the most recently calculated path
                else:

                    # Setting value of the next direction     
                    pathCopy = optimalPath[count]
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
                            
                    # If somehow the agent is trapped between future fires states, we call the new path that goes through the future fire so the agent is not stuck
                    if (future_spread[x+1, y] != 0) and (future_spread[x-1, y] != 0) and (future_spread[x, y+1] != 0) and (future_spread[x, y-1] != 0):
                        optimalPath = bfs(spread_maze, currentPos, goal, mlen)
                    else:
                    # If not, the path recalculated starts from the closest free state cell (indicated by 0) to the goal
                        optimalPath = bfs(future_spread, currentPos, goal, mlen)

                    # Setting the new direction value from the new calculated path
                    pathCopy = optimalPath[0]
                    # Converting new first direction to a tuple value
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Finding the x,y of the new tuple value (x,y)
                    x = currentPos[0]
                    y = currentPos[1]
                    # Resetting the count back to 1 just incase if we do not need a path recalculation instantly 
                    count = 1

                    # If the newly returned path tells us not path exists then the Agent is trapped and can no longer reach the goal
                    if(optimalPath == "No such path from S to G exists."):
                        optimalPath = f"No such path from {x}, {y} to G exists."
                        return optimalPath
                
                # If the current cell has no future fire state cells then we simply keep following the most recently calculated path
                else:
                        
                    # Setting value of the next direction 
                    pathCopy = optimalPath[count]
                    # Converting it into a tuple
                    currentPos = pathToPosition(pathCopy, x, y)
                    # Setting the x, y of the tuple (x,y) we made
                    x = currentPos[0]
                    y = currentPos[1]
                    # Incrementing count by 1 if we keep following the same path so we get the next direction in line
                    count += 1
                
    # If the initial path found no successful path, we return that it's not possible to get from S to G
    else:
        response = "No such path from S to G exists."
        return response

    # If the current position tuple is the goal tuple it means the agent made it from S to G!
    if (currentPos == goal):
        response = "Agent survived!"
        return response

def stratTwoBfs(maze, optimalpath, goal, mlen, q):

    # Copy of maze to call spread fire on
    spread_maze = maze

    # Retreiving first direction of movement from A* initial path
    pathCopy = optimalpath[0]

    # Converting current direction value to a tuple value
    currentPos = pathToPosition(pathCopy, 0, 0)

    # When a path exists from S to G
    if(optimalpath != "No such path from S to G exists."):
        while (currentPos != goal):

            # x,y tuple values from current position
            x = currentPos[0]
            y = currentPos[1]

            # Spreading fire 1 step on the maze we are working with
            spread_maze = spread_fire(spread_maze, q)

            # If the fire spreads onto the agent they die 
            if(spread_maze[x,y] == 2):
                response = "Agent died!"
                return response

            # Finding the new path after every time step
            newBfsPath = bfs(spread_maze, currentPos, goal, mlen)

            # If the newly returned path tells us not path exists then the Agent is trapped and can no longer reach the goal
            if(newBfsPath == "No such path from S to G exists."):
                return newBfsPath

            # Setting value of the new direction from the new path
            pathCopy = newBfsPath[0]
            # Converting the new direction into a tuple value
            currentPos = pathToPosition(pathCopy, x, y)

    # If the initial path found no successful path, we return that it's not possible to get from S to G
    else:
        response = "No such path from S to G exists."
        return response

    # If the current position tuple is the goal tuple it means the agent made it from S to G!
    if (currentPos == goal):
        response = "Agent survived!"
        return response

# take the maze, start, goal, and length of one side as parameters
def bfs(main_maze, start, goal, mlen):

    maze = copy.deepcopy(main_maze)

    # Initialize the queue and set the start and empty path string
    queue = deque([[start, ""]])

    # create a visited set (can do with list too) 
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
        # if the goal is found, return the path
        if node == goal:
            return path #, len(visited) # the number of nodes explored by BFS

        # keep getting an out of bounds axis error
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue

         # if the node is blocked or on fire, skip it and move on
        if maze[x, y] >= 1:
            continue

         # if the node is empty and hasnt been visited yet, add its neighbours to the queue
        elif maze[x, y] == 0 and node not in visited:
            visited.add(node)
            for movement, neighborElements in tree[node]:
                # path = current path + new movement, doing it outside the append broke it randomly
                queue.append((neighborElements, path + movement))
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

    # if no path is found
    return "No such path from S to G exists" #, int(len(visited)) # for number of nodes explored by BFS

# take the maze, start, goal, and length of one side as parameters
# marking visited nodes as 1 but could also just use a visited set and add the nodes as it traverses
def bfs_original(maze, start, goal, mlen):
    queue = deque([start])
    visited = np.zeros((mlen, mlen))
    while queue:

        x, y = queue.popleft()

        # if the goal is found, return true
        if (x, y) == goal:
            return True

        # keep getting an out of bounds axis error
        if x >= mlen or y >= mlen or x < 0 or y < 0:
            continue;

        # if the node is blocked, on fire, or already visited, skip it and move on
        if maze[x,y] >= 1 or visited[x, y] == 1:
            continue

        # if the node is empty and hasnt been visited yet, add its neighbours to the queue with right/down prio
        elif maze[x,y] == 0 and visited[x, y] == 0:
            visited[x,y] = 1
            queue.append((x+1, y)) # add right
            queue.append((x, y+1)) # add down
            queue.append((x, y-1)) # add up
            queue.append((x-1, y)) # add left

   # plt.imshow(visited)
   # plt.show()
    return False
