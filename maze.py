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

    plotting()

    # main_maze, mlen = mazeGen.mazeGen()
    # # Using matplotlib to visualize the Maze in a grid view
    # # plt.imshow(main_maze)
    # # plt.show()
    # main_maze, fire_initial = mazeGen.initialFire(main_maze, len(main_maze))

    # start = (0,0)
    # goal = (mlen-1, mlen-1)

    # # dfs checks if one point to another is reachable or not
    # fire_reachable = dfs(main_maze, start, fire_initial, mlen)
    # print(f'Is there a path from agent to fire {fire_initial} using DFS?: {fire_reachable}')
    # reachable = dfs(main_maze, start, goal, mlen)
    # print(f'Is there a path from {start} to {goal} using DFS?: {reachable}')

    #bfs returns the optimal path from the start to the goal
    #optimalpath = bfs(main_maze, start, goal, mlen)
    #print(f'Was a shortest path found from {start} to {goal}?: {optimalpath}')

    #colored_maze = colorPath(optimalpath, main_maze)
    #plt.imshow(colored_maze)
    #plt.show()

    # # A* returning the optimal path from S to G
    # aStarPath = aStar(main_maze, start, goal)
    # print(f'Is there a path from {start} to {goal} using A*?: {aStarPath}')
    # color_maze = colorPath(aStarPath, main_maze, 0, 0)
    # plt.imshow(color_maze)
    # plt.show()

    #fired = future_fire(color_maze)
    #plt.imshow(fired)
    #plt.show()

    #answer2 = stratTwoAStar(main_maze, aStarPath, goal)
    #print (answer2)

    # answer3 = stratThreeAStar(main_maze, aStarPath, goal)
    # print (answer3)


def plotting():
    flammability = [x * 0.1 for x in range(1, 10)]
    average = []

    mazelength = int(input("Enter the length of a square maze: "))

    # for each flammability 
    for x in range(1, 10):
        q = x * 0.1
        getQ(q)

        mazes = []

        # generate maze 10 times
        for y in range(0, 10):
            # generate a map
            main_maze, mlen = mazeGen.mazeGen(mazelength)
            # put initial fire
            maze, fire_initial = mazeGen.initialFire(main_maze, mlen)

            # check if there is a path from the agent to the initial fire
            fire_reachable = dfs(maze, (0,0), fire_initial, mlen)
            # check if there is a path from the agent to the goal 
            reachable = dfs(maze, (0,0), (mlen-1, mlen-1), mlen)

            # regenerate the maze until they are reachable from one another
            while (not fire_reachable) or (not reachable):
                main_maze, mlen = mazeGen.mazeGen(mazelength)
                maze, fire_initial = mazeGen.initialFire(main_maze, mlen)
                fire_reachable = dfs(maze, (0,0), fire_initial, mlen)
                reachable = dfs(maze, (0,0), (mlen-1, mlen-1), mlen)

            # if reachable, append mazes list
            mazes.append(maze)
            # plt.imshow(maze)
            # plt.show()

        success_count = 0
        # for each valid maze 
        for currMaze in mazes:
            # run algo 
            # current status: strat 2, A*
            aStarPath = aStar(currMaze, (0,0), (mlen-1, mlen-1))
            aStarPath2 = stratTwoAStar(currMaze, aStarPath, (mlen-1, mlen-1), q)
            # print(aStarPath2)
            if "survived" in aStarPath2:
                success_count += 1

        avg = success_count/10
        average.append(avg)
    
    plt.scatter(flammability, average, marker='o')
    plt.xlabel('Flammability q')
    plt.ylabel('Average success')
    plt.title('Strategy 2 of A* Algorithm')
    plt.show()

if __name__ == "__main__":
    main()