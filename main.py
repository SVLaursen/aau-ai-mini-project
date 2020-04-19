# 1: Print out map and ask the player to move in direction
# 2: Player moves in direction
# 3: Agent comes out of waiting state
# 4: Agent calculates path to player
# 5: Agent moves one tile towards the player
# 6: Agent goes into waiting state again and the cycle continues unless a goal has been met

# Player Goal: To survive in the map without getting caught by the agent until the round limit is achieved
# Agent Goal: To catch the player before the turn limit is up

# A = Agent, P = Player, # = Border, * = Path point, ^ = Obstacle

from MapConversion import *
from Player import *
from Agent import *

def print_maze(path = None):
    # Create the map to print
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if x == player.x and y == player.y:
                maze[x][y] = 3
            elif maze[x][y] == 3 and x != player.x and y != player.y:
                maze[x][y] = 0

            if path is not None:
                for i in range(len(pathlist)):
                    if i == 0:
                        continue
                    if x == pathlist[i][0] and y == pathlist[i][1] and maze[x][y] != 3:
                        maze[x][y] = 2

            if x == agent.x and y == agent.y:
                maze[x][y] = 4

    # make a pretty map to display
    prettyMaze = ConvertNumbersToMap(maze)

    # Print the map
    for i in range(len(prettyMaze)):
        print(prettyMaze[i])

print('Welcome to this showcase of the A* algorithm and Finite State Machine')
print('write start to start, exit to exit, and help if you want to know more')

inMenu = True
terminate = False

while inMenu:
    menuInput = input('-->')

    if menuInput == "start":
        inMenu = False
    elif menuInput == "exit":
        terminate = True
        inMenu = False
    elif menuInput == "help":
        print('play the game by writen: up, down, left, or right to move around')
        print('the goal is not to get caught by the agent, marked with an A')
        print('you play as the P on the map')
        print('# marks obstacles')
        print('good luck')
    else:
        print('!!Error on input, try a different command!!')


if not terminate:

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
    agent.world = maze

    active = True
    inputActive = True
    start_print = False
    turns = 0

    #Start runtime loop
    while active:

        #Executing agent behaviour
        agent.execute()
        agent.target = (player.x, player.y)

        if not start_print:
            print_maze()
            start_print = True

        if inputActive == False:
            #Check if the agent has caught the player
            if agent.x == player.x and agent.y == player.y:
                print('AGENT HAS CAUGHT YOU, GAME OVER!')
                active = False

            # Clean the map before usage
            for x in range(len(maze)):
                for y in range(len(maze[x])):
                    if maze[x][y] == 2 or maze[x][y] == 3 or maze[x][y] == 4:
                        maze[x][y] = 0

            if isinstance(agent.fsm.currentState, PathfindingState):
                continue

            if isinstance(agent.fsm.currentState, WaitState):
                agent.activate()
                continue

            path = agent.path

            if path is not None:
                pathlist = [list(i) for i in path]

            print_maze(path)

        if active:
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
            turns += 1

print('YOU SURVIVED FOR ' + str(turns) + ' TURNS!!!!!')
print('..............................................')