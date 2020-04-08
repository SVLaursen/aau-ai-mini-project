from random import randint
from time import clock


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
        print('executing wait state')


class PathfindingState(State):

    def __init__(self, fsm):
        super(PathfindingState, self).__init__(fsm)

    def Enter(self):
        print('Starting pathfinding state')
        super(PathfindingState, self).Enter()

    def Execute(self):
        #Tell the agent to calculate the path
        print('executing pathfinding state')
        self.fsm.transitionTo('toMoving')


class MoveState(State):

    def __init__(self, fsm):
        super(MoveState, self).__init__(fsm)

    def Enter(self):
        print('Starting moving state')
        super(MoveState, self).Enter()

    def Execute(self):
        print('executing moving state')
        self.fsm.transitionTo('toWait')