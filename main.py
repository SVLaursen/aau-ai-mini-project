# 1: Print out map and ask the player to move in direction
# 2: Player moves in direction
# 3: Agent comes out of waiting state
# 4: Agent calculates path to player
# 5: Agent moves one tile towards the player
# 6: Agent goes into waiting state again and the cycle continues unless a goal has been met

# Player Goal: To survive in the map without getting caught by the agent until the round limit is achieved
# Agent Goal: To catch the player before the turn limit is up

# A = Agent, P = Player, # = Border, * = Path point, ^ = Obstacle

# TODO: Create world array creater with obstacles
# TODO: Create finite state machine for the Agent
# TODO: Create player class
# TODO: Parse string inputs for the player input
# TODO: Print out the different states as the agent goes through them
# TODO: Find a way to color the array output so that the player can see where the agent will go according to A*
# TODO: Implement A* pathfinding for the agent

from AStar import *

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

from MapConversion import *

#Map is 10x10 making (9,9) the extreme point
start = (0, 0)
end = (9, 5)

path = AStar(maze, start, end)

for i in range(len(maze)):
    print(maze[i])

newMap = ConvertAStarMap(maze, path)

for i in range(len(newMap)):
    print(newMap[i])

#print(pathList)
#print(path)