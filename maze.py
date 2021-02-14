from PIL.Image import new
from mazeGen import *
import mazeGen
from aStar import * 
from aStarCopy import * 
from dfs import *
from bfs import *
from fire import *
from matplotlib import pyplot as plt
from matplotlib import colors


def pathToPosition(position, x, y):
    
    posCopy = position

    for element in posCopy:
        if(element == 'D'):
            x = x+1
        if(element == 'R'):
            y = y+1
        if(element == 'U'):
            x = x-1
        if(element== 'L'):
            y = y-1

    return (x,y)

def main():

    main_maze, mlen = mazeGen.mazeGen()
    # Using matplotlib to visualize the Maze in a grid view
    # plt.imshow(main_maze)
    # plt.show()

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfs checks if one point to another is reachable or not
    # reachable = dfs(main_maze, start, goal, mlen)
    # print(f'Is there a path from {start} to {goal} using DFS?: {reachable}')

    #bfs returns the optimal path from the start to the goal
    #optimalpath = bfs(main_maze, start, goal, mlen)
    #print(f'Was a shortest path found from {start} to {goal}?: {optimalpath}')

    #colored_maze = colorPath(optimalpath, main_maze)
    #plt.imshow(colored_maze)
    #plt.show()

    # A* returning the optimal path from S to G
    aStarPath = aStar(main_maze, start, goal)
    print(f'Is there a path from {start} to {goal} using A*?: {aStarPath}')
    color_maze = colorPath(aStarPath, main_maze, 0, 0)
    plt.imshow(color_maze)
    plt.show()


    spread_maze = main_maze

    newStart = (0,0)

    pathCopy = aStarPath[0]
    reach = 0

    currentPos = pathToPosition(pathCopy, 0, 0)

    x = 0
    y = 0

    if(aStarPath != "No such path from S to G exists."):
        while (currentPos != goal):

            spread_maze = spread_fire(spread_maze)

            newAStarPath = aStar(spread_maze, currentPos, goal)

            if(newAStarPath == "No such path from S to G exists."):
                print( "No such path from S to G exists.")
                break

            pathCopy = newAStarPath[0]

            x = currentPos[0]
            y = currentPos[1]

            currentPos = pathToPosition(pathCopy, x, y)

            color_maze = colorPath(newAStarPath, spread_maze, x, y)
            plt.imshow(color_maze)
            plt.show()

    if (currentPos == goal):
        print("Agent survived!")


if __name__ == "__main__":
    main()