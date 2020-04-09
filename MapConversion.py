

def ConvertNumbersToMap(numberMap):
    prettyMap = numberMap

    for y in range(len(numberMap)):
        for x in range(len(numberMap[y])):
            if numberMap[x][y] == 0:
                prettyMap[x][y] = '-'
            elif numberMap[x][y] == 1:
                prettyMap[x][y] = '#'

    return prettyMap


def ConvertAStarMap(worldMap, starPath):
    newMap = worldMap
    pathList = [list(i) for i in starPath]

    for y in range(len(worldMap)):
        for x in range(len(worldMap[y])):
            for p in range(len(pathList)):
                pos_x = pathList[p][0]
                pos_y = pathList[p][1]

                if pos_x == x and pos_y == y:
                    newMap[x][y] = '*'
                elif newMap[x][y] == 1:
                    newMap[x][y] = '#'

    for y in range(len(newMap)):
        for x in range(len(newMap[y])):
            if newMap[x][y] == 0:
                newMap[x][y] = '-'

    return newMap
