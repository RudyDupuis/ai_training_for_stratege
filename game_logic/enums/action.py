from enum import Enum


class Action(Enum):
    MOVE = "move"
    KILL = "kill"
    ROTATE = "rotate"
    PUSH = "push"
    PULL = "pull"


class ReceivedAction(Enum):
    IS_PUSHED = "isPushed"
    IS_PULLED = "isPulled"
    IS_KILLED = "isKilled"
