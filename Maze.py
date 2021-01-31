from MazeGen import *
import MazeGen
from dfs import *

def main():

    main_maze, mlen = MazeGen.mazeGen()
    # main_maze = MazeGen.maze
    # mlen = MazeGen.maze_length

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfs checks if one point to another is reachable or not
    reachable = dfs(main_maze, start, goal, mlen)
    print(f'Is there a path from {start} to {goal}?: {reachable}')

if __name__ == "__main__":
    main()