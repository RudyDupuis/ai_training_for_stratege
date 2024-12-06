from enum import Enum


class Action(Enum):
    Move = "move"
    Kill = "kill"
    Rotate = "rotate"
    Push = "push"
    Pull = "pull"


class ReceivedAction(Enum):
    IsPushed = "isPushed"
    IsPulled = "isPulled"
    IsKilled = "isKilled"
