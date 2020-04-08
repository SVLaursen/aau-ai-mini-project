#State parent object
#State = type("State", (object), {})

# --------------------------------------------------------------------


class Transition(object):

    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print('transitioning to ' + self.toState)

# --------------------------------------------------------------------


class FiniteStateMachine(object):

    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.previousState = None
        self.trans = None

    def AddTransition(self, transitionName, transition):
        self.transitions[transitionName] = transition

    def AddState(self, stateName, state):
        self.states[stateName] = state

    def SetState(self, stateName):
        self.previousState = self.currentState
        self.currentState = self.states[stateName]

    def transitionTo(self, transition):
        self.trans = self.transitions[transition]

    def Execute(self):
        if self.trans is not None:
            self.currentState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.currentState.Enter()
            self.trans = None
        self.currentState.Execute()

