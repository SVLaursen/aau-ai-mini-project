

def ConvertNumbersToMap(numberMap):

    prettyMap = [[0 for x in range(len(numberMap))] for y in range(len(numberMap[0]))]

    for x in range(len(numberMap)):
        for y in range(len(numberMap[x])):
            if numberMap[x][y] == 0:
                prettyMap[x][y] = '-'
            elif numberMap[x][y] == 1:
                prettyMap[x][y] = '#'
            elif numberMap[x][y] == 2:
                prettyMap[x][y] = '*'
            elif numberMap[x][y] == 3:
                prettyMap[x][y] = 'P'
            elif numberMap[x][y] == 4:
                prettyMap[x][y] = 'A'

    return prettyMap

