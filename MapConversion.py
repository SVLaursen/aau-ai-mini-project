

def ConvertNumbersToMap(numberMap):
    prettyMap = numberMap

    for y in range(len(numberMap)):
        for x in range(len(numberMap[y])):
            if numberMap[x][y] == 0:
                prettyMap[x][y] = '-'
            elif numberMap[x][y] == 1:
                prettyMap[x][y] = '#'

    return prettyMap


def ConvertAStarMap(worldMap, starPath, player):
    newMap = worldMap
    pathList = None

    if starPath is not None:
        pathList = [list(i) for i in starPath]

    for x in range(len(worldMap)):
        for y in range(len(worldMap[x])):

            if pathList is not None:
                for p in range(len(pathList)):
                    pos_x = pathList[p][0]
                    pos_y = pathList[p][1]

                    if pos_x == x and pos_y == y:
                        newMap[x][y] = '*'
                    elif newMap[x][y] == 1:
                        newMap[x][y] = '#'

            if player.x == x and player.y == y:
                newMap[x][y] = 'P'
            elif worldMap[x][y] == '1':
                newMap[x][y] = '#'

    for y in range(len(newMap)):
        for x in range(len(newMap[y])):
            if newMap[x][y] == 0:
                newMap[x][y] = '-'

    return newMap
