from PIL.Image import new
from mazeGen import *
import mazeGen
from aStar import * 
from dfs import *
from bfs import *
from fire import *
from matplotlib import pyplot as plt
from matplotlib import colors

def main():

    main_maze, mlen, fire_initial = mazeGen.mazeGen()
    # Using matplotlib to visualize the Maze in a grid view
    # plt.imshow(main_maze)
    # plt.show()

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfs checks if one point to another is reachable or not
    fire_reachable = reachable = dfs(main_maze, start, fire_initial, mlen)
    print(f'Is there a path from agent to fire {fire_initial} using DFS?: {fire_reachable}')
    reachable = dfs(main_maze, start, goal, mlen)
    print(f'Is there a path from {start} to {goal} using DFS?: {reachable}')

    #bfs returns the optimal path from the start to the goal
    # optimalpath = bfs(main_maze, start, goal, mlen)
    # print(f'Was a shortest path found from {start} to {goal}?: {optimalpath}')

    #colored_maze = colorPath(optimalpath, main_maze)
    #plt.imshow(colored_maze)
    #plt.show()

    # A* returning the optimal path from S to G
   # aStarPath = aStar(main_maze, start, goal)
   # print(f'Is there a path from {start} to {goal} using A*?: {aStarPath}')
    # color_maze = colorPath(optimalpath, main_maze, 0, 0)
    # plt.imshow(color_maze)
    # plt.show()


    # answer = stratTwoBfs(main_maze, optimalpath, goal, mlen)

    # print (answer)


if __name__ == "__main__":
    main()