# 1: Print out map and ask the player to move in direction
# 2: Player moves in direction
# 3: Agent comes out of waiting state
# 4: Agent calculates path to player
# 5: Agent moves one tile towards the player
# 6: Agent goes into waiting state again and the cycle continues unless a goal has been met

# Player Goal: To survive in the map without getting caught by the agent until the round limit is achieved
# Agent Goal: To catch the player before the turn limit is up

# A = Agent, P = Player, # = Border, * = Path point, ^ = Obstacle

# TODO: Create finite state machine for the Agent
# TODO: Create player class
# TODO: Parse string inputs for the player input
# TODO: Print out the different states as the agent goes through them
# TODO: Find a way to color the array output so that the player can see where the agent will go according to A*
# TODO: Implement A* pathfinding for the agent

from AStar import *
from MapConversion import *
from Player import *
from Agent import *


maze = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

#Map is 10x10 making (9,9) the extreme point
start = (0, 0)
end = (9, 5)

#Set player
player = Player()
player.world = maze
player.x = 7
player.y = 5

#Set the agent
agent = Agent()
agent.__init__()
agent.world = maze

active = True
inputActive = False

#Start runtime loop
while active:

    #Executing agent behaviour
    agent.execute()
    agent.target = (player.x, player.y)

    if inputActive == False:
        # Clean the map before usage
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == 2 or maze[x][y] == 3 or maze[x][y] == 4:
                    maze[x][y] = 0

        if isinstance(agent.fsm.currentState, MoveState):
            continue

        if isinstance(agent.fsm.currentState, WaitState):
            agent.activate()
            continue

        #path = AStar(maze, start, (player.x, player.y))
        path = agent.path

        if path is not None:
            pathlist = [list(i) for i in path]

        #Create the map to print
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if x == player.x and y == player.y:
                    maze[x][y] = 3
                elif maze[x][y] == 3 and x != player.x and y != player.y:
                    maze[x][y] = 0

                if path is not None:
                    for i in range(len(pathlist)):
                        if x == pathlist[i][0] and y == pathlist[i][1] and maze[x][y] != 3:
                            maze[x][y] = 2

                if x == agent.x and y == agent.y:
                    maze[x][y] = 4

        #Print the map
        for i in range(len(maze)):
            print(maze[i])

    inputActive = True

    while inputActive:
        userInput = input('-->')
        if userInput == "left" or userInput == "right" or userInput == "up" or userInput == "down":
            player.userInput = userInput
            if player.ParseInput():
                inputActive = False
            else:
                print('Move not possible, try again..')
        elif userInput == "exit":
            active = False
            inputActive = False
        else:
            print('invalid command, try again')

#print(pathList)
#print(path)