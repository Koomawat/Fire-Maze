from mazeGen import *
import mazeGen
from aStar import * 
from dfs import *
from bfs import *

def main():

    main_maze, mlen = mazeGen.mazeGen()

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfs checks if one point to another is reachable or not
    reachable = dfs(main_maze, start, goal, mlen)
    print(f'Is there a path from {start} to {goal} using DFS?: {reachable}')

    # bfs returns the optimal path from the start to the goal
    optimalpath = bfs(main_maze, start, goal, mlen)
    print(f'Was a shortest path found from {start} to {goal}?: {optimalpath}')

    # A* returning the optimal path from S to G
    aStarPath = aStar(main_maze, start, goal)
    print(f'Is there a path from {start} to {goal} using A*?: {aStarPath}')




if __name__ == "__main__":
    main()