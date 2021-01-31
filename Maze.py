from mazeGen import *
import mazeGen
from dfs import *

def main():

    main_maze, mlen = mazeGen.mazeGen()

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfs checks if one point to another is reachable or not
    reachable = dfs(main_maze, start, goal, mlen)
    print(f'Is there a path from {start} to {goal}?: {reachable}')

if __name__ == "__main__":
    main()