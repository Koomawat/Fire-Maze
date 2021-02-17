from PIL.Image import new
from mazeGen import *
import mazeGen
from aStar import * 
from dfs import *
from bfs import *
from fire import *
from matplotlib import pyplot as plt
from matplotlib import colors


def path():
    maze_length = int(input("Enter the length of a square maze: "))
    main_maze, mlen = mazeGen.mazeGen(maze_length)
    q = float(input("Enter the flammability of the maze: "))
    main_maze, fire_initial = mazeGen.initialFire(main_maze, len(main_maze))
    
    # Using matplotlib to visualize the Maze in a grid view
    plt.imshow(main_maze)
    plt.show()
    

    start = (0,0)
    goal = (mlen-1, mlen-1)

    # dfsCheck(main_maze, start, goal, fire_initial, mlen)

    # bfsCheck(main_maze, start, goal, mlen, q)

    # a1Check(main_maze, start, goal)

    # fired = future_fire(color_maze, q)
    # plt.imshow(fired)
    # plt.show()
    
    aStarPath = a1Check(main_maze, start, goal)
    a2Check(main_maze, aStarPath, goal, q)

    print('---------------------')

    aStarPath = a1Check(main_maze, start, goal)
    a3Check(main_maze, aStarPath, goal, q)


def main():

    # plotting()

    path()
    

def plotting():
    flammability = [x * 0.1 for x in range(1, 10)]
    average = []

    mazelength = int(input("Enter the length of a square maze: "))

    # for each flammability 
    for x in range(1, 10):
        q = x * 0.1

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

            # strat 1, A*
            aStarPath = aStar(currMaze, (0,0), (mlen-1, mlen-1))
            # if "No" not in aStarPath:
            #     success_count += 1
            # plt.title('Strategy 1, A* Algorithm')
            
            # strat 2
            # aStarPath2 = stratTwoAStar(currMaze, aStarPath, (mlen-1, mlen-1), q)
            # if "survived" in aStarPath2:
            #     success_count += 1
            # plt.title('Strategy 2, A* Algorithm')

            # strat 3
            aStarPath3 = stratThreeAStar(currMaze, aStarPath, (mlen-1, mlen-1), q, '')
            print (aStarPath3)
            if "survived" in aStarPath3:
                success_count += 1
            plt.title('Strategy 3, A* Algorithm')

        avg = success_count/10
        average.append(avg)
    
    plt.scatter(flammability, average, marker='o')
    plt.xlabel('Flammability q')
    plt.ylabel('Average success')
    # plt.title('Strategy 2, A* Algorithm')
    plt.show()

def dfsCheck(main_maze, start, goal, fire_initial, mlen):
    # # dfs checks if one point to another is reachable or not
    # fire_reachable = dfs(main_maze, start, fire_initial, mlen)
    # print(f'Is there a path from agent to fire {fire_initial} using DFS?: {fire_reachable}')
    reachable = dfs(main_maze, start, goal, mlen)
    print(f'Is there a path from {start} to {goal} using DFS?: {reachable}')

    dfs_path = dfs_graph(main_maze, start, goal, mlen)
    colored_maze = colorPath(dfs_path, main_maze, 0, 0)
    plt.imshow(colored_maze)
    plt.show()



def bfsCheck(main_maze, start, goal, mlen, q):
    # bfs returns the optimal path from the start to the goal
    optimalpath = bfs(main_maze, start, goal, mlen, q)
    print(f'Was a shortest path found from {start} to {goal}?: {optimalpath}')

    colored_maze = colorPath(optimalpath, main_maze, 0, 0)
    plt.imshow(colored_maze)
    plt.show()

def a1Check(main_maze, start, goal):
    # A* returning the optimal path from S to G
    aStarPath = aStar(main_maze, start, goal)
    print(f'Is there a path from {start} to {goal} using A*?: {aStarPath}')

    color_maze = colorPath(aStarPath, main_maze, 0, 0)
    plt.imshow(color_maze)
    plt.show()
    
    return aStarPath

def a2Check(main_maze, aStarPath, goal, q):
    answer2, msg, fire_maze = stratTwoAStar(main_maze, aStarPath, goal, q, '')
    print('answer2: ' + msg)

    colormap = colorPath(answer2, fire_maze, 0, 0)
    plt.imshow(colormap)
    plt.show()

def a3Check(main_maze, aStarPath, goal, q):
    answer3, msg, fire_maze = stratThreeAStar(main_maze, aStarPath, goal, q, '')
    print('answer3: ' + msg)

    colormap = colorPath(answer3, fire_maze, 0, 0)
    plt.imshow(colormap)
    plt.show()

if __name__ == "__main__":
    main()