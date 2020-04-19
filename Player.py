class Player(object):

    def __init__(self):
        self.world = 0
        self.x = 0
        self.y = 0
        self.userInput = ''

    def CheckMovementInput(self, x, y):
        if len(self.world) <= x or len(self.world[0]) <= y:
            return False
        elif self.world[x][y] == 1:
            return False
        return True

    def ParseInput(self):
        if self.userInput == 'left':
            if not self.CheckMovementInput(self.x - 1, self.y):
                return False
            self.x -= 1
            return True
        elif self.userInput == 'right':
            if not self.CheckMovementInput(self.x + 1, self.y):
                return False
            self.x += 1
            return True
        elif self.userInput == 'up':
            if not self.CheckMovementInput(self.x, self.y + 1):
                return False
            self.y += 1
            return True
        elif self.userInput == 'down':
            if not self.CheckMovementInput(self.x, self.y - 1):
                return False
            self.y -= 1
            return True

