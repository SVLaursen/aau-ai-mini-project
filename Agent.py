from FiniteStateMachine import *
from States import *


class Agent(object):

    def __init__(self):
        # initialization logic
        self.fsm = FiniteStateMachine(self)

        #States
        self.fsm.states["Wait"] = WaitState(self.fsm)
        self.fsm.states["Pathfinding"] = PathfindingState(self.fsm)
        self.fsm.states["Moving"] = MoveState(self.fsm)

        #Transitions
        self.fsm.AddTransition('toWait', Transition("Wait"))
        self.fsm.AddTransition('toPathfinding', Transition("Pathfinding"))
        self.fsm.AddTransition('toMoving', Transition("Moving"))

        self.fsm.SetState('Wait')

    def execute(self):
        self.fsm.Execute()

    def activate(self):
        self.fsm.transitionTo('toPathfinding')



