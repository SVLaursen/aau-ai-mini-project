from FiniteStateMachine import *
from States import *


class Agent(object):

    def __init__(self):
        # initialization logic
        self.fsm = FiniteStateMachine(self)

        #States
        self.fsm.states["Wait"] = WaitState(self.fsm)
        self.fsm.states["Pathfinding"] = PathfindingState(self.fsm, self)
        self.fsm.states["Moving"] = MoveState(self.fsm, self)

        #Transitions
        self.fsm.AddTransition('toWait', Transition("Wait"))
        self.fsm.AddTransition('toPathfinding', Transition("Pathfinding"))
        self.fsm.AddTransition('toMoving', Transition("Moving"))

        #Set initial starting state
        self.fsm.SetState('Wait')

        #Class properties
        self.world = None
        self.path = None
        self.x = 0
        self.y = 0
        self.target = None

    def execute(self):
        self.fsm.Execute()

    def activate(self):
        print('activating')
        self.fsm.transitionTo('toPathfinding')

    def setposition(self, x, y):
        self.x = x
        self.y = y



