from random import randint
from time import clock
from AStar import *


class State(object):
    def __init__(self, fsm):
        self.fsm = fsm
        self.timer = 0
        self.startTime = 0

    def Enter(self):
        self.timer = randint(0, 5)
        self.startTime = int(clock())


    def Execute(self):
        pass

    def Exit(self):
        pass


class WaitState(State):

    def __init__(self, fsm):
        super(WaitState, self).__init__(fsm)

    def Enter(self):
        print('Starting wait state')
        super(WaitState, self).Enter()

    def Execute(self):
        super(WaitState, self).Execute()

class PathfindingState(State):

    def __init__(self, fsm, agent):
        super(PathfindingState, self).__init__(fsm)
        self.agent = agent

    def Enter(self):
        print('Starting pathfinding state')
        super(PathfindingState, self).Enter()

    def Execute(self):
        #Tell the agent to calculate the path
        print('executing pathfinding state')

        #TODO: Take the maze from the parent agent class and calculate a map
        self.agent.path = AStar(self.agent.world, (self.agent.x, self.agent.y), self.agent.target)

        #End current state and transition to moving state
        self.fsm.transitionTo('toMoving')


class MoveState(State):

    def __init__(self, fsm, agent):
        super(MoveState, self).__init__(fsm)
        self.agent = agent

    def Enter(self):
        print('Starting moving state')
        super(MoveState, self).Enter()

    def Execute(self):
        #Move the agent to the next point on the path
        convertedpath = [list(i) for i in self.agent.path]
        self.agent.setposition(convertedpath[1][0], convertedpath[1][1])

        print('Moving towards target')

        self.fsm.transitionTo('toWait')