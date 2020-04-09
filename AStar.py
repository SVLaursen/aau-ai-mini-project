
# -- Node for the A* algorithm --
class Node(object):

    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

# -- A* Algorithm --
def AStar(maze, start, end):
    startNode = Node(None, start)
    endNode = Node(None, end)

    openList = []
    closedList = []

    openList.append(startNode)

    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openList.pop(currentIndex)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode

            while current is not None:
                path.append(current.position)
                current = current.parent

            return path[:: -1] #return the path reversed

        children = []

        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (
                    len(maze[len(maze) - 1]) - 1) or nodePosition[1] < 0:
                continue

            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode = Node(currentNode, nodePosition)
            children.append(newNode)

        for child in children:
            for closedChild in closedList:
                if child == closedChild:
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            openList.append(child)
